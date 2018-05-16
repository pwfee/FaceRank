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
  fpp_detected = models.IntegerField(default=0)


class FaceInfo(models.Model):
  image = models.ForeignKey('ImageModel')
  face_score = models.FloatField(default=0)
  like_count = models.PositiveIntegerField(default=0)


class FacePlusPlusInfo(models.Model):
  image = models.ForeignKey('ImageModel')
  smile = models.FloatField(default=0)
  age = models.IntegerField(default=0)
  gender = models.IntegerField(default=0)
  beauty_male_score = models.FloatField(default=0)
  beauty_female_score = models.FloatField(default=0)
