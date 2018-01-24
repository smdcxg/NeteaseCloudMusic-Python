#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取用户粉丝列表

'''

def load(obj):
    obj.user_getfolloweds = user_getfolloweds

def user_getfolloweds(self, uid=0, offset=0, limit=30):
    url = 'http://music.163.com/weapi/user/getfolloweds/'
    params = {
      'userId': uid,
      'offset': offset,
      'limit': limit,
      "csrf_token": ''
    }
    return self.post(url, None, params)
