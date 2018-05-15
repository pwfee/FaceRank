# coding:utf-8
import cv2
import dlib
import utils.const
from math import fabs
from utils.models import ImageModel, FaceInfo
from utils.shortcuts import cacl_mid_point, cacl_distance
from utils.const import *


class RaterDispatcher:
  def __init__(self, _img_id):
    self.image = ImageModel.objects.get(id=_img_id)
    self.img_path = os.path.join(settings.UPLOAD_DIR, self.image.file_name)
    self.landmark_predictor = dlib.shape_predictor(
      utils.const.LANDMARK_PREDICTOR_MODEL_PATH)

  def face_detector(self):
    img = cv2.imread(self.img_path)
    detector = dlib.get_frontal_face_detector()
    faces = detector(img, 1)

    if len(faces) > 0:
      if len(faces) == 1:
        self.image.status = utils.const.SINGLE_FACE_FOUND
        shape = self.landmark_predictor(img, faces[0])
        self.facial_rater(shape)
      else:
        self.image.status = utils.const.FOUND_TOO_MANY_FACES
    else:
      self.image.status = utils.const.FACE_NOT_FOUND
    self.image.save()

  def facial_rater(self, shape):
    eyebrow_mid = cacl_mid_point(shape.part(left_eyebrow_right_corner),
                                 shape.part(right_eyebrow_left_corner))
    d1 = cacl_distance(shape.part(nose_contour_lower_middle), eyebrow_mid)
    d2 = cacl_distance(shape.part(left_eye_right_corner),
                       shape.part(right_eye_left_corner))
    d3 = cacl_distance(shape.part(nose_left), shape.part(nose_right))
    d4 = cacl_distance(shape.part(contour_left1), shape.part(contour_right1))
    d5 = cacl_distance(shape.part(contour_chin),
                       shape.part(nose_contour_lower_middle))
    d6_left = cacl_distance(shape.part(left_eye_left_corner),
                            shape.part(left_eye_right_corner))
    d6_right = cacl_distance(shape.part(right_eye_left_corner),
                             shape.part(right_eye_right_corner))
    d7 = cacl_distance(shape.part(mouth_left_corner),
                       shape.part(mouth_right_corner))
    d8 = cacl_distance(shape.part(contour_left4), shape.part(contour_right4))

    init_score = 100
    deduction = 0

    # 眼角距离为脸宽的 1/5，
    deduction += fabs((d2 / d4) * 100 - 25)

    # 鼻子宽度为脸宽的 1/5
    deduction += fabs((d3 / d4) * 100 - 25)

    # 眼睛的宽度，应为同一水平脸部宽度的 1/5
    eye_dist_avg = (d6_left + d6_right) / 2
    deduction += fabs(eye_dist_avg / d4 * 100 - 25)

    # 理想嘴巴宽度应为同一脸部宽度的 1/2
    deduction += fabs((d7 / d8) * 100 - 50)

    # 下巴到鼻子下方的高度 == 眉毛中点到鼻子最低处的距离
    deduction += fabs(d5 - d1)

    face_info = FaceInfo(image=self.image)
    face_info.face_score = init_score - deduction + 20
    face_info.save()