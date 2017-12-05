#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from .config import *
from .components import load_components
from .drive import load_drive

class OPC(object):    # 网易云音乐操作类
    def __init__(self):
        #self.headers = HEADERS.copy()     # 请求头

        self.cellphone_link = "http://music.163.com/weapi/login/cellphone?csrf_token="
        self.playlist_link = PLAYLIST_LINK                           # 发现音乐-歌单链接
        self.comment_link = COMMENTS_LINK                            # 评论链接
        self.search_link = SEARCH_LINK                               # 搜索链接
        self.search_suggest_link = SEARCH_SUGGEST_LINK               # 搜索建议链接
        self.palylist_param = PLAYLIST_PARAM.copy()
        self.playlist_param_limit_size = PLAYLIST_PARAM_LIMIT_SIZE
        self.comment_param = COMMENTS_PARAM.copy()
        self.comment_param_limit_size = COMMENTS_PARAM_LIMIT_SIZE
        self.cellphone_login_param = CELLPHONE_LOGIN_PARAM
        self.search_param = SEARCH_PARAM
        self.search_suggest_param = SEARCH_SUGGEST_PARAM

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
    def get_discover(self, classif=None):    # 获取网易云音乐 发现音乐-歌单 歌单id
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
       
load_components(OPC)
load_drive(OPC)
