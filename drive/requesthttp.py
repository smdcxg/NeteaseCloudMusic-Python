#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from ..config import *
from ..core import *
from .returnvalue import ReturnValue

def load_requestHttp(obj):
    req = RequestHttp()
    obj.post = req.post
    obj.get = req.get

class RequestHttp(object):
    
    def __init__(self):
        self.headers = HEADERS.copy()     # 请求头

        self.csrf_token = ""    # token
        if SESSION_EN:    # 是否开启session回话
            self.s = requests.Session()
        else:
            self.s = requests

    def post(self, url=None, dheaders=None, dparams=None):
        self.headers['Referer'] = url
        payload = get_post_param(dparams)
        req = self.s.post(url, headers=(dheaders if dheaders != None else self.headers), params = payload)
        data = {"ret":""}    # ReturnValue 采用回填数据方式
        ret = ReturnValue(data, req)
        return data["ret"]
    
    def get(self, url=None, dheaders=None, dparams=None):
        self.headers['Referer'] = url
        req = self.s.get(url, headers=(dheaders if dheaders != None else self.headers), params = dparams)
        return req
     
    def get_headers(self):
        return self.headers;
