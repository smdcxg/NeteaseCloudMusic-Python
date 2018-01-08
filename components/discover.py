
import re
import json

def load(obj):
    obj.get_discover      = get_discover

def get_discover(self, classifIndex=0, params=None):    # 获取网易云音乐 发现音乐
    classif_func_key = str(self.discover_classif[classifIndex])
    url = eval('self.discover_'+classif_func_key+'_link')
    real_params = eval('self.discover_'+classif_func_key+'_params')
    if params:
        for key, value in params.items():
            if value:
                real_params[str(key)] = value

    r = self.post(url, None, real_params)
    return r
