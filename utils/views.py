# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

import logging
import os
import utils.const

from rater.tasks import face_detect
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
    image, _ = utils.models.ImageModel.objects.get_or_create(file_name=imgFile.name)

    face_detect.delay(image.id)
    return self.response({
      "success": True,
      "msg": utils.const.IMAGE_UPLOAD_SUCCESS
    })



