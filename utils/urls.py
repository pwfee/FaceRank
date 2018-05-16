from django.conf.urls import url

from .views import ImageUploadAPIView, ImageCheck

urlpatterns = [
    url(r"^upload_image/?$", ImageUploadAPIView.as_view(), name="upload_image"),
    url(r"^image_status/?$", ImageCheck.as_view(), name="image_status")
]
