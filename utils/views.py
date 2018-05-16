# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

import logging
import os
import utils.const

from rater.tasks import face_detect_task, face_plus_plus_detect_task
from utils.api import CSRFExemptAPIView
from utils.models import ImageUploadForm
from utils.shortcuts import rand_str

logger = logging.getLogger(__name__)


class ImageUploadAPIView(CSRFExemptAPIView):
  request_parsers = ()

  def post(self, request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
      img = form. cleaned_data["image"]
    else:
      return self.response({
        "success": False,
        "msg": utils.const.IMAGE_UPLOAD_INVALID,
        "file_path": ""
      })

    suffix = os.path.splitext(img.name)[-1].lower()
    if suffix not in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]:
      return self.response({
        "success": False,
        "msg": utils.const.IMAGE_UPLOAD_UNSUPPORTED_FORMAT,
        "file_path": ""
      })

    img_name = rand_str(10) + suffix

    try:
      with open(os.path.join(settings.UPLOAD_DIR, img_name), "wb") as imgFile:
        for chunk in img:
          imgFile.write(chunk)
    except IOError as e:
      logger.error(e)
      return self.response({
        "success": True,
        "msg": utils.const.IMAGE_UPLOAD_SERVER_ERROR
      })

    # 保存照片上传信息
    image, _ = utils.models.ImageModel.objects.get_or_create(file_name=img_name)

    face_detect_task.delay(image.id)

    # 若启用 FACE_PLUS_PLUS 接口
    if utils.const.FACE_PLUS_PLUS_ENABLE:
      face_plus_plus_detect_task.delay(image.id)

    return self.response({
      "files": [{
        "success": True,
        "name": img_name,
        "image_id": image.id,
        "msg": utils.const.IMAGE_UPLOAD_SUCCESS,
        "url": "http://" + request.get_host() + "/face/" + str(image.id),
        "type": "image/png",
        "thumbnailUrl": "http://" + request.get_host() + "/static/upload/" + img_name
      }]
    })


class ImageCheck(CSRFExemptAPIView):
  request_parsers = ()

  def get(self, request):
    image_id = request.GET.get('id', None)

    image = utils.models.ImageModel.objects.filter(id=image_id).first()

    res = {}

    if not image:
      res.update({"image_status": utils.const.IMAGE_NOT_FOUND})
    else:
      res.update({"image_status": utils.const.IMAGE_EXIST,
                  "face_status": image.status})
      if image.status == utils.const.SINGLE_FACE_FOUND:
        face = utils.models.FaceInfo.objects.get(image=image)
        res.update({"score": face.face_score})

    return self.response(res)




