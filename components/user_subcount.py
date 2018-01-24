#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取用户信息 , 歌单，收藏，mv, dj 数量

'''

def load(obj):
    obj.user_subcount = user_subcount

def user_subcount(self):
    url = 'http://music.163.com/weapi/subcount'
    params = {
      "csrf_token": ''
    }
    return self.post(url, None, params)
