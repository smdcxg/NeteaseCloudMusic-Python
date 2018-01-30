＃NeteaseCloudMusic-python
<br />
网易云音乐python版Api

# 开发文档
[^_^]:
	### > 获取精彩评论
	```python
	req_hotComment(music_id)
	```
	##### 参数：
	`music_id`：音乐id
	##### 返回数据格式：
	```python

	```


### > 获取最新评论
```python
req_comments(music_id, page = 1, page_num = 20, comments_type = 0)
```
##### 参数：
`music_id`：id   （音乐填写音乐id， 评论填写评论id）<br>
`page`：第几页<br>
`page_num`：每页数量<br>
`comments_type`：0/1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 - 音乐评论     1 - 歌单评论<br>

<br>

### > 获取全部评论
```python
req_all_comments(music_id, page_num = 100, comments_type = 0)
```
##### 说明：迭代进行
##### 参数：
`music_id`：id    （音乐填写音乐id， 评论填写评论id）<br>
`page_num`：每次迭代的数量<br>
`comments_type `：0/1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 - 音乐评论     1 - 歌单评论<br>

<br>

### 歌单列表
```python
playlist(order='hot', cat='全部', limit='50', offset=0)
```
##### 说明：获取网易云 发现音乐-歌单 <br>
##### 地址：`http://music.163.com/weapi/playlist/list`<br />
##### 参数：<br>
`order`：歌单类别（最热=hot    最新=new）<br>
`cat`：
```**语种** >> 华语| 欧美| 日语| 韩语| 粤语| 小语种|

**风格** >> 流行| 摇滚| 民谣| 电子| 舞曲| 说唱| 轻音乐| 爵士| 乡村| R&B/Soul| 古典| 民族| 英伦| 金属| 朋克| 蓝调| 雷鬼| 世界音乐| 拉丁| 另类/独立| New Age| 古风| 后摇| Bossa Nova|

**场景** >> 清晨| 夜晚| 学习| 工作| 午休| 下午茶| 地铁| 驾车| 运动| 旅行| 散步| 酒吧|

**情感** >> 怀旧| 清新| 浪漫| 性感| 伤感| 治愈| 放松| 孤独| 感动| 兴奋| 快乐| 安静| 思念|

**主题** >> 影视原声| ACG| 校园| 游戏| 70后| 80后| 90后| 网络歌曲| KTV| 经典| 翻唱| 吉他| 钢琴| 器乐| 儿童| 榜单| 00后|
```

`limit`：每页数量

`offset`：偏移位置

