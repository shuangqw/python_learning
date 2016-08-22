# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import re
import urllib
import tablib
from bs4 import BeautifulSoup

#爬取地址
taobao_url = 'https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.w2.3.DWOa80&n_s=new'

#获取整个网页源码 并转为utf-8编码
soup = BeautifulSoup(urllib.urlopen(taobao_url),"html.parser")
movie_page = soup.get_text().encode('utf-8')


#获取电影名称，评分，详情等信息
movie_name = soup.select('.movie-card-name .bt-l')
movie_score = soup.select('.movie-card-name .bt-r')


#表格初始化
headers = ('名称', '评分', '导演', '主演', '类型', '地区', '语言', '片长')


#存储影片名称
_movie_name = open('movie_name.txt','a+')

for i in movie_name:
  name = re.search(r'>([^<]+)',str(i))
  _movie_name.write(name.group(1))
  _movie_name.write('\n')


# #存储评分
_movie_score = open('movie_score.txt','a+')

for i in movie_score:
  score = re.search(r'>([^<]+)',str(i))
  _movie_score.write(score.group(1))
  _movie_score.write('\n')


#正则获取导演、主演、类型、地区、语言、片长信息

director_list = re.findall(ur'导演：(.+)'.encode('utf-8'),movie_page)
actor_list = re.findall(ur'主演：(.+)'.encode('utf-8'),movie_page)
type_list = re.findall(ur'类型：(.+)'.encode('utf-8'),movie_page)
area_list = re.findall(ur'地区：(.+)'.encode('utf-8'),movie_page)
lang_list = re.findall(ur'语言：(.+)'.encode('utf-8'),movie_page)
time_list = re.findall(ur'片长：(.+)'.encode('utf-8'),movie_page)

#将导演、主演、类型、地区、语言、片长信息存储到txt中
def save_txt(_file_name, _list):
  for x in _list:
    _file_name.write(x)
    _file_name.write('\n')
  return _file_name

director_name = open('director_name.txt','a+')
actor_name = open('actor_name.txt','a+')
type_name = open('type_name.txt','a+')
area_name = open('area_name.txt','a+')
lang_name = open('lang_name.txt','a+')
time_name = open('time_name.txt','a+')

save_txt(director_name, director_list)
save_txt(actor_name, actor_list)
save_txt(type_name, type_list)
save_txt(area_name, area_list)
save_txt(lang_name, lang_list)
save_txt(time_name, time_list)


#再次将指针定位到文件开头
_movie_name.seek(0, 0)
_movie_score.seek(0, 0)
director_name.seek(0, 0)
actor_name.seek(0, 0)
type_name.seek(0, 0)
area_name.seek(0, 0)
lang_name.seek(0, 0)
time_name.seek(0, 0)

#将影片信息保存到表格中
data = []
for i in xrange(1,len(movie_name)+1):
  tup = (_movie_name.readline(), _movie_score.readline(), director_name.readline(), actor_name.readline(), type_name.readline(), area_name.readline(), lang_name.readline(),time_name.readline())
  data.append(tup)

mylist = tablib.Dataset(*data, headers=headers)

_movie_test = open('movie.xls', 'wb')
with _movie_test as f:
  f.write(mylist.xls)

#关闭所有开启的文件
_movie_name.close()
_movie_name.close()
director_name.close()
actor_name.close()
type_name.close()
area_name.close()
lang_name.close()
time_name.close()
_movie_test.close()
