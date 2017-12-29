from .core import Core
from .playlistcore import playListCore

instanceList = []

def newCore():
    core = Core()
    instanceList.append(core)
    return core
def newPCore():
    pcore = playListCore()
    instanceList.append(pcore)
    return pcore
    

# core编码操作
originCore = newCore()
get_post_param = originCore.get_post_data

# textarea 内容解码
pCore = newPCore()
decodeTextComponent = pCore.decodeURIComponent
