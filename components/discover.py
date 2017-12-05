
import re

def load_discover(obj):
    obj.get_discover = get_discover

def get_discover(self, classif="playlist", params=None):    # 获取网易云音乐 发现音乐
    data = []
    r = self.get(self.playlist_link, None, params)
    #res_p = r'<p class="dec">\n<a.*?href=\".*?id=(.*?)\".*?>(.*?)</a>\n</p>'
    #res_p = r'<div class="u-cover u-cover-1">\n<img class="j-flag" src="(.*?)"/>\n<a title="(.*?)".*?\
    #data-res-type="(.*?)"\ndata-res-id="(.*?)".*?<span class="nb">(.*?)</span>'
    res_p = r'<div class="u-cover u-cover-1">(.*?)</div>'
    a = re.findall(res_p, r.text, re.S)
    '''for i in range(len(a)):
        data.append({"img_url":a[i][0], "class_title":a[i][1], "class_id":a[i][3], "type":a[i][2], "nb":a[i][4]})
    client = MongoClient('localhost', 27017)
    db = client.music_class
    db.collection_names(include_system_collections=False)
    music_class_db = db.music_class
    result = music_class_db.insert_many(data)'''
    print(len(a))
    print(a)
    #w = core.core()
    #r = requests.post("http://music.163.com/weapi/v1/resource/comments/R_SO_4_193012?csrf_token=d4702f0c6da20e024c8da6db0cbfa400", params=w.get_post_data())
    #
    #print(r.content)
