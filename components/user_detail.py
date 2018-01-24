#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取用户详情

'''

def load(obj):
    obj.user_detail = user_detail

def user_detail(self, uid=0):
    url = 'http://music.163.com/weapi/v1/user/detail/'+uid
    params = {
      "csrf_token": ''
    }
    return self.post(url, None, params)
