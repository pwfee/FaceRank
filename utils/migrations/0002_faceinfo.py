# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-15 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_score', models.FloatField(default=0)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.ImageModel')),
            ],
        ),
    ]
