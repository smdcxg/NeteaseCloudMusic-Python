from .core import Core

instanceList = []

def new_Core():
    core = Core()
    instanceList.append(core)
    return core

# core编码操作
originCore = new_Core()
get_post_param = originCore.get_post_data
