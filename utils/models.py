# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


# Create your models here.
class ImageUploadForm(forms.Form):
  image = forms.FileField()