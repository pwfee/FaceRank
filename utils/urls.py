from django.conf.urls import url

from .views import ImageUploadAPIView

urlpatterns = [
    url(r"^upload_image/?$", ImageUploadAPIView.as_view(), name="upload_image")
]
