#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..core import *

def load_search(obj):
    obj.search = search
    obj.search_suggest = search_suggest
def search(self, condition=None):

    # search_param_set    ----START
    self.search_param["s"] = condition
    self.search_param["csrf_token"] = self.csrf_token
    # search_param_set    ----END
    r = self.post(self.search_link, dheaders = None, dparams = self.search_param)
    return r    

def search_suggest(self, condition=None, limit=8):

    # search_suggest_param_set    ----START 
    self.search_suggest_param["s"] = condition
    self.search_suggest_param["limit"] = str(limit)
    self.search_suggest_param["csrf_token"] = self.csrf_token
    # search_suggest_param_set    ----END
    r = self.post(self.search_suggest_link, dheaders = None, dparams = self.search_suggest_param)
    return r 
