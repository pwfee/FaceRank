from __future__ import absolute_import, unicode_literals
from celery import shared_task
from rater.dispatcher import RaterDispatcher, FacePlusPlusRaterDispatcher


@shared_task
def face_detect_task(img_id):
  RaterDispatcher(img_id).face_detector()


@shared_task
def face_plus_plus_detect_task(img_id):
  FacePlusPlusRaterDispatcher(img_id).fpp_detector()