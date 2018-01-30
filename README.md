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
