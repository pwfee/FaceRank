# -*- coding: UTF-8 -*-

import os
import re
import datetime
from math import pow, sqrt
import random
from base64 import b64encode
from io import BytesIO

from django.utils.crypto import get_random_string


class Point2D:
  def __init__(self, x_init=0, y_init=0):
    self.x = x_init
    self.y = y_init


def rand_str(length=32, type="lower_hex"):
  """
  生成指定长度的随机字符串或者数字, 可以用于密钥等安全场景
  :param length: 字符串或者数字的长度
  :param type: str 代表随机字符串，num 代表随机数字
  :return: 字符串
  """
  if type == "str":
    return get_random_string(length,
                             allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
  elif type == "lower_str":
    return get_random_string(length,
                             allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789")
  elif type == "lower_hex":
    return random.choice("123456789abcdef") + get_random_string(length - 1,
                                                                allowed_chars="0123456789abcdef")
  else:
    return random.choice("123456789") + get_random_string(length - 1,
                                                          allowed_chars="0123456789")


def cacl_distance(p1, p2):
  return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2))


def cacl_mid_point(p1, p2):
  res_mid_point = Point2D()
  res_mid_point.x = (p1.x + p2.x) / 2
  res_mid_point.y = (p1.y + p2.y) / 2
  return res_mid_point