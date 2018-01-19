#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def load(obj):
    obj.discover_playlist = playlist

def playlist(self, order='hot', cat='全部', limit='50', offset=0):
    url = "http://music.163.com/weapi/playlist/list"    # 网易云音乐歌单列表
    
    real_params = {
      "order": order,
      "cat": cat,
      "limit": limit,
      "offset": offset
    }

    r = self.post(url, None, real_params)
    return r
    

