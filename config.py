VERSION = "1.0.0"
SESSION_EN = True    # 开启session回话请求模式

CELLPHONE_LOGIN_PARAM = {
    "phone":"",
    "password":"",
    "rememberLogin":True
}

DISCOVER            = ["playlist", "toplist", "artist", "album"]
COMMENTS_TYPE                = ["A_PL_0","R_SO_4"]  # 0-歌单评论列表   1-歌曲评论列表
PLAYLIST_LINK                = "http://music.163.com/playlist/"    # 网易云音乐歌单列表

COMMENTS_LINK                = "http://music.163.com/weapi/v1/resource/comments/"    # 评论链接
SEARCH_SUGGEST_LINK          = "http://music.163.com/weapi/search/suggest/web?csrf_token="   # 搜索链接
SEARCH_LINK                  = "http://music.163.com/weapi/cloudsearch/get/web?csrf_token="

COMMENTS_PARAM = {    # 评论post数据格式
    "rid": "",
    "offset": "0",
    "total": "true",
    "limit": "20",
    "csrf_token": ""
}

DISCOVER_PLAYLIST_PARAMS = {    # 发现音乐-歌单 post数据格式
    "order":"hot",
    "cat":"全部",
    "limit":35,
    "offset":0
}

SEARCH_SUGGEST_PARAM = {
    "s":"",
    "limit":"",
    "csrf_token":"",
}

SEARCH_PARAM = {
    "hlposttag":"</span>",
    "hlpretag":'<span class="s-fc7">',
    "limit":"30",
    "offset":"0",
    "s":"",
    "total":"true",
    "type":"1",
    "csrf_token":"",
}

PRIVATE_FM_LINK = 'http://music.163.com/weapi/v1/radio/get'

HEADERS = {
    "accept":"*/*",
    "accept-encoding":"gzip, deflate",
    "accept-language":"zh-cn,zh;q=0.8",
    "cache-control":"max-age=0",
    "connection":"keep-alive",
    "host":"music.163.com",
    "upgrade-insecure-requests":"1",
    "user-agent":'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtmL, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
