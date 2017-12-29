
import re
import json
from ..core import *


def load_playlist(obj):
    obj.get_playlist      = get_playlist


def get_playlist(self, playListID=None):
    data = []
    params = {"id":playListID}
    r = self.get(self.playlist_link, None, params)
    res_p = r'<div class="m-info f-cb" id="auto-id-(\w{4}).*?">\n<div class="cover u-cover u-cover-dj">\n<img.*?data-key="(.*?)"'
    dataKeys = re.findall(res_p, r.text)
    if dataKeys:
        textarea = re.findall(r'<textarea style="display:none;">(.*?)</textarea>', r.text, re.S)
        a = decodeTextComponent(textarea[0], "".join(dataKeys[0]))
    return a
