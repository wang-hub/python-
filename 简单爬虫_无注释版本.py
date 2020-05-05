# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:18:30 2020

@author: wangwei
"""

from bs4 import BeautifulSoup as bs
import urllib.request

headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

url="http://www.baidu.com/s?"
key=input("请输入想爬内容:")
page=1
data = {'wd':key,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
key_code = urllib.parse.urlencode(data)
url=url+key_code
res=urllib.request.Request(url)
data=urllib.request.urlopen(res).read().decode("utf-8","ignore")

soup=bs(data,features="lxml")
items=soup.find_all(class_='t')  
print(items) 
for item in items:
        print(item.text.replace(" ",''))