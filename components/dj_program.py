#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取用户电台

'''

def load(obj):
    obj.dj_program = dj_program

def dj_program(self, uid=0):
    url = 'http://music.163.com/weapi/dj/program/'+str(uid)
    params = {
      "csrf_token": ''
    }
    return self.post(url, None, params)
