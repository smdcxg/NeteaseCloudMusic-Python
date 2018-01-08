#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymongo
import json
import os
from pymongo import MongoClient

def load(obj):
    obj.url                   = url
    obj.req_comments          = req_comments
    obj.req_all_comments      = req_all_comments
    obj.req_comment           = req_comment

def url(self, comments_type = 0, mid = ""):
    if mid:
        return "%s%s_%s?csrf_token=%s" % (self.comment_link, self.comments_type[comments_type], mid, self.csrf_token)

def req_hotComment(self, music_id):    # 获取精彩评论
    comments = self.req_comment(music_id, 1, 1, 1)
    comments.pop("comments")
    comments.pop("total")
    comments.pop("more")
    return comments

def req_comments(self, music_id, page, page_num, comments_type):    # 获取最新评论
    comments = self.req_comment(music_id, page, page_num, comments_type)
    comments.pop("moreHot")
    comments.pop("hotComments")
    return comments

def req_all_comments(self, music_id, page_num = 100, comments_type = 0):    # 获取网易云音乐全部 评论
    ret_data = []
    page = 1
    comments = self.req_comment(music_id, page, page_num, comments_type)
    while True:
        yield comments
        if comments["more"]:
            page += 1
            comments = self.req_comment(music_id, page, page_num, comments_type)
        else:
            return 

def req_comment(self, music_id = "", page = 1, page_num = 20, comments_type = 0):    # 获取网易云音乐 评论data
    url = self.url(comments_type, music_id)

    #comment_param_set    ----START
    self.comment_param["rid"] = music_id
    self.comment_param["offset"] = (page - 1) * page_num
    self.comment_param["total"] = "true"
    self.comment_param["limit"] = page_num
    self.comment_param["csrf_token"] = self.csrf_token
    #comment_param_set    ----END

    #payload = get_post_param(self.comment_param)
    #r = self.s.post(url, headers=self.headers, params=payload)
    r = self.post(url, dheaders=None, dparams=self.comment_param)
    return r

'''
    def set_comment_param(self, rid = "", page = 1, page_num = 20,  csrf_token = ""):
        if page_num >= self.comment_param_limit_size["min"] and page_num <= self.comment_param_limit_size["max"]:
            self.comment_param["rid"] = rid
            self.comment_param["offset"] = (page - 1) * page_num
            self.comment_param["total"] = "true"
            self.comment_param["limit"] = page_num
            self.comment_param["csrf_token"] = csrf_token
        else:
            self.comment_param["offset"] = cfg.COMMENTS_PARAM["offset"]
            self.comment_param["limit"] = cfg.COMMENTS_PARAM["page_num"]
'''
