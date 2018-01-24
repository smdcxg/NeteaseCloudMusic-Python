#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取最近 5 个听了这首歌的用户

'''

def load(obj):
    obj.discovery_simiUser = discovery_simiUser

def discovery_simiUser(self, sid=0):
    url = 'http://music.163.com/weapi/discovery/simiUser'
    params = {
      'songid': str(sid),
    }
    return self.post(url, None, params)
