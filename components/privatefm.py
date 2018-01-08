#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def load(obj):
    obj.get_privateFM = privateFM


def privateFM(self):
    return self.post(self.private_fm_link, None, {'csrf_token':''})
