#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   获取每日推荐歌曲

'''

def load(obj):
    obj.recommend_songs = recommend_songs

def recommend_songs(self, offset=0, limit=20):
    url = 'http://music.163.com/weapi/v1/discovery/recommend/songs'
    params = {
      'offset': offset,
      'total': True,
      'limit': limit,
      "csrf_token": ''
    }
    return self.post(url, None, params)
