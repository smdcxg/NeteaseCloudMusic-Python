#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

def load(obj):
    obj.login = login

def login(self, phone=None, passWord=None, rememberLogin=True):
    
    # cellphone_login_param_set    ----START
    self.cellphone_login_param["phone"] = phone
    self.cellphone_login_param["password"] = md5(passWord)
    self.cellphone_login_param["rememberLogin"] = rememberLogin
    # cellphone_login_param_set    ----END
    ret = self.post(self.cellphone_link, dheaders=None, dparams=self.cellphone_login_param)
    
    return ret

def md5(str):
    m = hashlib.md5()   
    m.update(str.encode("utf-8"))
    return m.hexdigest()
