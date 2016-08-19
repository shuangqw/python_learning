# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import re
import urllib
from bs4 import BeautifulSoup

taobao_url = 'https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.w2.3.DWOa80&n_s=new'

soup = BeautifulSoup(urllib.urlopen(taobao_url),"html.parser")
# utf_soup = soup.decode('utf-8')
movie_pic = soup.find_all('div',class_='movie-card-poster')
movie_tag = soup.select('.movie-card-list > span')
movie_name = soup.select('.movie-card-name > span')


movie_name_str = str(movie_name)

movie_page = soup.get_text().encode('utf-8')
name_str = re.findall(r'导演:([^\\n])+',movie_page)

# change_to_utf8_name = name_str.decode('utf-8')
# print name_str.read()
# a = name_str.read()

# print name_str

myfile1 = open('movieabc.txt','w')
myfile1.write(str(name_str))
myfile1.close()

