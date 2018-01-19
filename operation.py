#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

import os, sys
sys.path.append(os.path.split(os.path.realpath(__file__))[0])

from .config import *
from .components import load_components
from .drive import load_drive

class OPC(object):    # 网易云音乐操作类
    def __init__(self):
        #self.headers = HEADERS.copy()     # 请求头

        self.cellphone_link = "http://music.163.com/weapi/login/cellphone?csrf_token="
        self.discover_classif = DISCOVER.copy()

        self.private_fm_link = PRIVATE_FM_LINK

        self.playlist_link = PLAYLIST_LINK                           # 歌单列表
        self.comment_link = COMMENTS_LINK                            # 评论链接
        self.search_link = SEARCH_LINK                               # 搜索链接
        self.search_suggest_link = SEARCH_SUGGEST_LINK               # 搜索建议链接
        self.comment_param = COMMENTS_PARAM.copy()
        self.cellphone_login_param = CELLPHONE_LOGIN_PARAM.copy()
        self.search_param = SEARCH_PARAM.copy()
        self.search_suggest_param = SEARCH_SUGGEST_PARAM.copy()

        self.comments_type = ["A_PL_0","R_SO_4"]  # 0-歌单评论列表   1-歌曲评论列表
        self.csrf_token = ""    # token
        '''if SESSION_EN:    # 是否开启session回话
            self.s = requests.Session()
        else:
            self.s = requests
        '''
    ''' Sing In-Operation
    '''

    def login(self, phone=None, passWord=None, rememberLogin=True):
        raise NotImplementedError()

    ''' Comment-Operation
        获取网易云评论
    '''
    def get_discover(self, classifIndex=None, toplistIndex=0):    # 获取网易云音乐 发现音乐-歌单
        raise NotImplementedError()

    def get_playlist(self, playListID=None):
        raise NotImplementedError()

    def url(self, comments_type=None, mid=None):
        raise NotImplementedError()

    def req_hotComment(self, music_id=None):    # 获取精彩评论
        raise NotImplementedError()

    def req_comments(self, music_id=None, page=None, page_num=None, comments_type=None):    # 获取最新评论
        raise NotImplementedError()

    def req_all_comments(self, music_id=None, page_num = 100, comments_type=0):    # 获取网易云音乐全部 评论
        raise NotImplementedError()

    def req_comment(self, music_id=None, page=1, page_num=20, comments_type=0):    # 获取网易云音乐 评论data
        raise NotImplementedError()

    def search(self, condition=None):           # 搜索
        raise NotImplementedError()

    def search_suggest(self, condition=None, limit=8):           # 搜索建议
        raise NotImplementedError()

    def post(self, url=None, dheaders=None, dparams=None):    # dpost
        raise NotImplementedError()
    
    def get(self, url=None, dheaders=None, dparams=None):    # dget
        raise NotImplementedError()

    def get_privateFM(self): # 私人FM
        raise NotImplementedError()
       
load_components(OPC)
load_drive(OPC)
