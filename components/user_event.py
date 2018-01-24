#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
    获取单个用户动态

'''

def load(obj):
    obj.user_event = event

def event(self, uid=0):
    url = 'http://music.163.com/weapi/event/get/'+uid
    params = {
      'time': -1,
      'getcounts': True,
      'csrf_token': ''
    }

    return self.post(url, None, params)
