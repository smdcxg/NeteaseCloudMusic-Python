#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获得歌词

'''

def load(obj):
    obj.lyric = lyric

def lyric(self, sid=0):
    url = 'http://music.163.com/weapi/song/lyric?os=osx&id=' + str(sid) + '&lv=-1&kv=-1&tv=-1'
    params = {
      
    }
    return self.post(url, None, params)
