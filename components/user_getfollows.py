#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取用户关注列表

'''

def load(obj):
    obj.user_getfollows = user_getfollows

def user_getfollows(self, uid=0, offset=0, limit=30):
    url = 'http://music.163.com/weapi/user/getfollows/'+str(uid)
    params = {
      'offset': offset,
      'limit': limit,
      'order': True,
      "csrf_token": ''
    }
    return self.post(url, None, params)
