#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def load(obj):
    obj.discover_toplist = toplist

def toplist(self, idx=0, limit=30, offset=0):
    url = "http://music.163.com/weapi/v3/playlist/detail"
    types = [
        ["云音乐新歌榜", "3779629"],
        ["云音乐热歌榜", "3778678"],
        ["网易原创歌曲榜", "2884035"],
        ["云音乐飙升榜", "19723756"],
        ["云音乐电音榜", "10520166"],
        ["UK排行榜周榜", "180106"],
        ["美国Billboard周榜", "60198"],
        ["KTV嗨榜", "21845217"],
        ["iTunes榜", "11641012"],
        ["Hit FM Top榜", "120001"],
        ["日本Oricon周榜", "60131"],
        ["韩国Melon排行榜周榜", "3733003"],
        ["韩国Mnet排行榜周榜", "60255"],
        ["韩国Melon原声周榜", "46772709"],
        ["中国TOP排行榜(港台榜)", "112504"],
        ["中国TOP排行榜(内地榜)", "64016"],
        ["香港电台中文歌曲龙虎榜", "10169002"],
        ["华语金曲榜", "4395559"],
        ["中国嘻哈榜", "1899724"],
        ["法国 NRJ EuroHot 30周榜", "27135204"],
        ["台湾Hito排行榜", "112463"],
        ["Beatport全球电子舞曲榜", "3812895"],
        ["云音乐ACG音乐榜", "71385702"],
        ["云音乐嘻哈榜", "991319590"]
    ]
    real_params = {
        'id':types[idx][1],
        'limit': limit,
        'offset': offset,
        'total': True,
        'n': 1000,
        'csrf_token': ""
    }

    r = self.post(url, None, real_params)
    return r
