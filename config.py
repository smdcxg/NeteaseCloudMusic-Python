VERSION = "1.0.0"
SESSION_EN = True    # 开启session回话请求模式

CELLPHONE_LOGIN_PARAM = {
    "phone":"",
    "password":"",
    "rememberLogin":True
}

DISCOVER            = ["playlist", "toplist", "artist", "album"]
DISCOVER_INFO       = {
    "playlist":{},
    "toplist":{},
    "artist":{
        "top":{
            "url":"http://music.163.com/weapi/artist/top?csrf_token=",
            "param":{
                
            }
        },
    },
    "album":{}
}
COMMENTS_TYPE                = ["A_PL_0","R_SO_4"]  # 0-歌单评论列表   1-歌曲评论列表
DISCOVER_PLAYLIST_LINK       = "http://music.163.com/discover/playlist/"    # 获取网易云音乐的链接 发现音乐-歌单
PLAYLIST_LINK                = "http://music.163.com/playlist/"    # 网易云音乐歌单列表
TOPLIST_LINK                 = "http://music.163.com/discover/toplist?id=19723756"
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
COMMENTS_PARAM_LIMIT_SIZE = {"min":1, "max":100}     # 评论post数据limit限制

PLAYLIST_PARAM = {    # 发现音乐-歌单post数据格式
    "order":"hot",
    "cat":"全部",
    "limit":35,
    "offset":0
}
PLAYLIST_PARAM_LIMIT_SIZE = {"min":1, "max":100}    # 发现音乐-歌单post数据格式limit限制

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
