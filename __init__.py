from .config import VERSION
from .operation import OPC

__version__ = VERSION

instanceList = []

def new_OPC():
    op_core = OPC()
    instanceList.append(op_core)
    return op_core

# 评论操作
originOPC            = new_OPC()

login                      = originOPC.login               # sign in
get_discover               = originOPC.get_discover            # 发现
get_comments               = originOPC.req_comments        # 最新评论
get_all_comments           = originOPC.req_all_comments    # 最新全部评论 
get_hot_comments           = originOPC.req_hotComment      # 精彩评论
search                     = originOPC.search              # 搜索 
search_suggest             = originOPC.search_suggest      # 搜索建议
get_playlist               = originOPC.get_playlist        # 获取playlist
