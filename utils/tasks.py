from __future__ import absolute_import, unicode_literals
from celery import shared_task
import cv2


@shared_task
def get_img_size(f):
  img = cv2.imread(f)
  return img.size
