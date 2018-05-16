#!/usr/bin/python
import requests
import utils.const


def fpp_detect(_file):
  url = utils.const.FACE_PLUS_PLUS_API_URL
  files = {'image_file': open(_file, 'rb')}
  data = {
    'api_key': utils.const.FACE_PLUS_PLUS_API_KEY,
    'api_secret': utils.const.FACE_PLUS_PLUS_API_SECRET,
    'return_attributes': utils.const.FACE_PLUS_PLUS_ATTRIBUTES
  }
  res = requests.post(url, data=data, files=files)
  return res