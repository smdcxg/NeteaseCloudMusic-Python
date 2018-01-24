#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取用户听歌排行

'''

def load(obj):
    obj.user_playRecord = playRecord

def playRecord(self, uid=0, types=0):
    url = 'http://music.163.com/weapi/v1/play/record'
    params = {
      "uid": str(uid),
      "type": types,
      "limit": 1000,
      "offset": 0,
      "total": True,
      "csrf_token": ''
    }
    return self.post(url, None, params)
