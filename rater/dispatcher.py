import cv2
import dlib
import utils.const
from utils.models import ImageModel


class RaterDispatcher:
  def __init__(self, _img_id):
    self.image = ImageModel.objects.get(id=_img_id)
    self.img_path = self.image.file_name

  def face_detector(self):
    img = cv2.imread(self.img_path)
    detector = dlib.get_frontal_face_detector()
    faces = detector(img, 1)

    if len(faces) > 0:
      if len(faces) == 1:
        # get_land_mark()
      else:
        print utils.const.FOUND_TOO_MANY_FACES
    else:
      print utils.const.FACE_NOT_FOUND

