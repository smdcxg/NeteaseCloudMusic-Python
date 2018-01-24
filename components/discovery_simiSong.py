#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取相似音乐

'''

def load(obj):
    obj.discovery_simiSong = discovery_simiSong

def discovery_simiSong(self, sid=0):
    url = 'http://music.163.com/weapi/v1/discovery/simiSong'
    params = {
      'songid': sid,
    }
    return self.post(url, None, params)
