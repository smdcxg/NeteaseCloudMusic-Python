
import re
import json

discover_classif_func = None

def load_discover(obj):
    obj.get_discover      = get_discover
    discover_func()

def discover_func():    # 映射函数
    global discover_classif_func
    discover_classif_func = {"playlist":discover_playlist, "toplist":discover_toplist, "artist":discover_artist, "album":discover_album}

def get_discover(self, classifIndex=0, params=None):    # 获取网易云音乐 发现音乐
    a = discover_classif_func[str(self.discover_classif[classifIndex])](self, params)
    '''for i in range(len(a)):
        data.append({"img_url":a[i][0], "class_title":a[i][1], "class_id":a[i][3], "type":a[i][2], "nb":a[i][4]})
    client = MongoClient('localhost', 27017)
    db = client.music_class
    db.collection_names(include_system_collections=False)
    music_class_db = db.music_class
    result = music_class_db.insert_many(data)'''
    return a

def discover_playlist(self, params=None):
    data = []
    r = self.get(self.discover_playlist_link, None, params)
    #res_p = r'<p class="dec">\n<a.*?href=\".*?id=(.*?)\".*?>(.*?)</a>\n</p>'
    res_p = r'<div class="u-cover u-cover-1">\n<img class="j-flag" src="(.*?)"/>\n<a title="(.*?)".*?data-res-type="(.*?)"\ndata-res-id="(.*?)".*?<span class="nb">(.*?)</span>'
    a = re.findall(res_p, r.text, re.S)
    return a

def discover_toplist(self, params=None):
    data = []
    req = self.get(self.toplist_link, None, params)
    res_p = r'<textarea style="display:none;">(.*?)</textarea>'
    a = re.findall(res_p, req.text, re.S)
    return json.loads(a[0])

def discover_artist(self, params=None):
    data = []
    r = self.post(self.discover_classif_info["artist"]["top"]["url"], None, params)
    return r

def discover_album(self, params=None):
    return 1
