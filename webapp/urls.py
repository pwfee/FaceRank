from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^/?$", webapp_index, name="index"),
    url(r"^about/?$", webapp_about, name="about"),
    url(r"^list/?$", webapp_face_list, name="list"),
    url(r"^judge/?$", webapp_judge, name="list"),
    url(r"^face/$", webapp_face_random, name="face"),
    url(r'^face/(?P<image_id>[^\/]+)/$', webapp_face_object, name='face_object'),
]
