# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import *
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from utils.models import ImageModel, FaceInfo
from utils.const import SINGLE_FACE_FOUND


def webapp_index(request):
  return render(request, 'index.html')


def webapp_about(request):
  return render(request, 'about.html')


def webapp_judge(request):
  return render(request, 'judge.html')


def webapp_face_list(request):
  page = request.GET.get('page', '1')
  limit = request.GET.get('limit', '20')
  faces = FaceInfo.objects.all().order_by('-face_score')
  _all = FaceInfo.objects.all().count()
  paginator = Paginator(faces, limit)

  current_page = int(page)
  all_pages = paginator.num_pages

  if all_pages < 7:
    page_range = range(1, all_pages + 1)

  else:
    if current_page < 5:
      page_range = range(1, 8)

    elif all_pages - current_page < 4:
      page_range = range(all_pages - 6, all_pages + 1)

    else:
      page_range = range(current_page - 3, current_page + 4)

  try:
    faces = paginator.page(page)  # 获取某页对应的记录
  except PageNotAnInteger:  # 如果页码不是个整数
    faces = paginator.page(1)  # 取第一页的记录
  except EmptyPage:  # 如果页码太大，没有相应的记录
    faces = paginator.page(paginator.num_pages)  # 取最后一页的记录

  return render(request, 'list.html',
                {'faces': faces, 'all': _all, "page_range": page_range,
                 "limit": limit})


def webapp_face_object(request, image_id):
    image = ImageModel.objects.filter(id=image_id, status=SINGLE_FACE_FOUND).order_by('?')[0]
    face = get_object_or_404(FaceInfo, image_id=image_id)
    _all = FaceInfo.objects.all()

    _count = _all.count()
    rank = FaceInfo.objects.filter(face_score__gt=face.face_score).count() + 1
    return render(request, 'face.html', {'image': image,
                                         'face': face,
                                         'rank': rank,
                                         'count': _count})


def webapp_face_random(request):
  image = ImageModel.objects.filter(status=SINGLE_FACE_FOUND).order_by('?')[0]
  face = FaceInfo.objects.get(image=image)
  rank = FaceInfo.objects.filter(face_score__gt=face.face_score).count() + 1
  _count = FaceInfo.objects.all().count()
  return render(request, 'face.html', {'image': image,
                                       'face': face,
                                       'rank': rank,
                                       'count': _count})

