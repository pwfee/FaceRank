# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models


class ImageUploadForm(forms.Form):
  image = forms.FileField()


class ImageModel(models.Model):
  file_name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(default=0)


class FaceInfo(models.Model):
  image = models.ForeignKey('ImageModel')
  face_score = models.FloatField(default=0)
  like_count = models.PositiveIntegerField(default=0)
