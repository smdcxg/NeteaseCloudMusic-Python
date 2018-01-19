#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def load(obj):
    obj.discover_playlist = playlist

def playlist(self, params={}):
    url = "http://music.163.com/weapi/playlist/list"    # 网易云音乐歌单列表
    
    real_params = {
      "order":"hot",
      "cat":"全部",
      "limit":35,
      "offset":0
    }

    if params:
        for key, value in params.items():
            if value:
                real_params[str(key)] = value
    r = self.post(url, None, real_params)
    return r
    

