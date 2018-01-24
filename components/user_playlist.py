#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

'''
    获取用户歌单列表

'''

def load(obj):
    obj.user_playlist = playlist

def playlist(self, uid, offset=0, limit=30):
    url = 'http://music.163.com/weapi/user/playlist'
    params = {
      'offset': offset,
      'uid': uid,
      'limit': limit,
      'csrf_token': '' 
    }
    r = self.post(url, None, params)
    return r
