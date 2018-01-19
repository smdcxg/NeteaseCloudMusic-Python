#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def load(obj):
    obj.discover_artist = artist

def artist(self, params={}):
    url = 'http://music.163.com/weapi/artist/top'
    real_params = {
      'offset': 0,
      'total': True,
      'limit': 30,
      'csrf_token': ''
    }

    if params:
        for key, value in params.items():
            if value:
                real_params[str(key)] = value
    r = self.post(url, None, real_params)
    return r
