#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ReturnValue(dict):
    
    dataDict = {}
    code = None

    def __init__(self, returnValueDict = {}, rawResponse=None):
        if rawResponse:
            try:
                self.dataDict = rawResponse.json()
            except ValueError:
                self.dataDict = {
                    'code':-101,
                    'errMsg':'Not JSON data!',
                    'data':rawResponse.content,
                }
        else:
            self.dataDict = {
                'code':-100,
                'errMsg':'rawResponse = None',
                'data':rawResponse,
            }
        
        self.code = self.dataDict['code']
        returnValueDict["ret"] = self.dataDict.copy()

    def __str__(self):
        return '%s' % self.code

    def __repr__(self):
        return '<NetEaseReturnValue: %s>' % self.__str__()
