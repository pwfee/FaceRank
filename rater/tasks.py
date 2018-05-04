from __future__ import absolute_import, unicode_literals
from celery import shared_task
from rater.dispatcher import RaterDispatcher


@shared_task
def face_detect(img_id):
  RaterDispatcher(img_id).face_detector()