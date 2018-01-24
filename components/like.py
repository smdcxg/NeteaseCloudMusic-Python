#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
   添加歌曲到‘我喜欢音乐’

'''

def load(obj):
    obj.like = like

def like(self, id, like=True, alg='itembased', time=25):
    url = 'http://music.163.com/weapi/radio/like?alg='+alg+'&trackId='+str(id)+'&like='+str(like)+'&time='+str(time)
    params = {
      "csrf_token": '',
      'trackId': str(id),
      'like': str(like),
    }
    return self.post(url, None, params)
