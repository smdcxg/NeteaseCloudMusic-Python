
＃NeteaseCloudMusic-python
<br />
网易云音乐python版Api

# 开发文档

### 获取最新评论
```python
req_comments(music_id, page = 1, page_num = 20, comments_type = 0)
```
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`music_id`**：id   （音乐填写音乐id， 评论填写评论id）<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`page`**：第几页<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`page_num`**：每页数量<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`comments_type`**：0/1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 - 音乐评论     1 - 歌单评论<br>

<br>

### 获取全部评论
```python
req_all_comments(music_id, page_num = 100, comments_type = 0)
```
**说明**：迭代进行<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`music_id`**：id    （音乐填写音乐id， 评论填写评论id）<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`page_num`**：每次迭代的数量<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`comments_type `**：0/1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 - 音乐评论     1 - 歌单评论<br>

<br>

### 歌单列表
```python
playlist(order='hot', cat='全部', limit='50', offset=0)
```
**说明**：获取网易云 发现音乐-歌单 <br>
**地址**：`http://music.163.com/weapi/playlist/list`<br />
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`order`**：歌单类别（最热=hot    最新=new）<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`cat`**：
```**语种** >> 华语| 欧美| 日语| 韩语| 粤语| 小语种|

**风格** >> 流行| 摇滚| 民谣| 电子| 舞曲| 说唱| 轻音乐| 爵士| 乡村| R&B/Soul| 古典| 民族| 英伦| 金属| 朋克| 蓝调| 雷鬼| 世界音乐| 拉丁| 另类/独立| New Age| 古风| 后摇| Bossa Nova|

**场景** >> 清晨| 夜晚| 学习| 工作| 午休| 下午茶| 地铁| 驾车| 运动| 旅行| 散步| 酒吧|

**情感** >> 怀旧| 清新| 浪漫| 性感| 伤感| 治愈| 放松| 孤独| 感动| 兴奋| 快乐| 安静| 思念|

**主题** >> 影视原声| ACG| 校园| 游戏| 70后| 80后| 90后| 网络歌曲| KTV| 经典| 翻唱| 吉他| 钢琴| 器乐| 儿童| 榜单| 00后|
```
&ensp;&ensp;&ensp;&ensp;&ensp;**`limit`**：每页数量<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`offset`**：偏移位置<br>

<br>

### 排行榜
```python
toplist(idx=0, limit=30, offset=0)
```
**说明**：获取发现音乐-排行<br>
**地址**：`http://music.163.com/weapi/v3/playlist/detail`<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`idx`**：--获取类型--<br>
	

	    0 - ["云音乐新歌榜", "3779629"],
    	1 - ["云音乐热歌榜", "3778678"],
    	2 - ["网易原创歌曲榜", "2884035"],
    	3 - ["云音乐飙升榜", "19723756"],
    	4 - ["云音乐电音榜", "10520166"],
    	5 - ["UK排行榜周榜", "180106"],
    	6 - ["美国Billboard周榜", "60198"],
    	7 - ["KTV嗨榜", "21845217"],
    	8 - ["iTunes榜", "11641012"],
    	9 - ["Hit FM Top榜", "120001"],
    	10 - ["日本Oricon周榜", "60131"],
    	11 - ["韩国Melon排行榜周榜", "3733003"],
    	12 - ["韩国Mnet排行榜周榜", "60255"],
    	13 - ["韩国Melon原声周榜", "46772709"],
    	14 - ["中国TOP排行榜(港台榜)", "112504"],
    	15 - ["中国TOP排行榜(内地榜)", "64016"],
    	16 - ["香港电台中文歌曲龙虎榜", "10169002"],
    	17 - ["华语金曲榜", "4395559"],
    	18 - ["中国嘻哈榜", "1899724"],
    	19 - ["法国 NRJ EuroHot 30周榜", "27135204"],
    	20 - ["台湾Hito排行榜", "112463"],
    	21 - ["Beatport全球电子舞曲榜", "3812895"],
    	22 - ["云音乐ACG音乐榜", "71385702"],
    	23 - ["云音乐嘻哈榜", "991319590"]
	
&ensp;&ensp;&ensp;&ensp;&ensp;**`limit`**：数量<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`offset`**：起始位置<br>

<br>

### 获取相似音乐
```python
discovery_simiSong(sid=0)
```
**说明**：获取跟当前歌曲（sid）相似的音乐<br>
**地址**：`http://music.163.com/weapi/v1/discovery/simiSong`<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`sid`**：音乐id

<br>

### 获取最近 5 个听了这首歌的用户
```python
discovery_simiUser(id)
```
**说明**：获取最近 5 个听了这首歌的用户（需要登录）<br>
**地址**：`http://music.163.com/weapi/discovery/simiUser`<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`sid`**：音乐id<br>

<br>

### 获取每日推荐歌曲
```python
recommend_songs()
```
**说明**：获取每日推荐歌单（需要登录）

<br>

### 喜欢音乐
```python
like(id, like=True, alg='itembased', time=25)
```
**说明**：音乐加入到 创建的歌单-我喜欢的音乐<br>
**地址**：`http://music.163.com/weapi/radio/like`<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`id`**：音乐id<br>

<br>

### 获取用户详情
```python
user_detail(uid=0)
```
**说明**：获取用户的详细信息<br>
**地址**：`http://music.163.com/weapi/v1/user/detail/`<br>
**参数**：
&ensp;&ensp;&ensp;&ensp;&ensp;**`uid`**：用户id<br>

<br>

### 获取用户关注列表
```python
user_getfollows(uid=0, offset=0, limit=30)
```
**说明**：获取用户关注列表<br>
**地址**：`http://music.163.com/weapi/user/getfollows/`<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`uid`**：用户id<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`limit`**：数量<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`offset`**：起始位置<br>

<br>

### 获取用户粉丝列表
```python
user_getfolloweds(uid=0, offset=0, limit=30)
```
**说明**：获取用户粉丝列表<br>
**地址**：`http://music.163.com/weapi/user/getfolloweds/`<br>
**参数**：<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`uid`**：用户id<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`limit`**：数量<br>
&ensp;&ensp;&ensp;&ensp;&ensp;**`offset`**：起始位置<br>
