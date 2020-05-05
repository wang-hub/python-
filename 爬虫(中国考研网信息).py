# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:09:31 2020

@author: wangwei
"""

import requests
from bs4 import BeautifulSoup
import re

#设置代理
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"}
#请求，建立soup对象
url='http://www.chinakaoyan.com/'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')
#提取信息
data=soup.find_all('div',attrs={'class':'soso_area_box'})
data=str(data)
#print(data)
pattern=re.compile(r'<a href="(.*?)".*?>(.*?)</a>',re.S)
inf_dir=pattern.findall(data)
#print(inf_dir)

'''
#匹配所有院校操作
for inf in inf_dir:
    #print(inf)
    url='http://www.chinakaoyan.com/'+inf[0]
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    data=soup.find_all('div',attrs={'class':'colu-info-body'})
    data=str(data)
    #print(data)
    #这里只匹配找出名称，后面修改
    pattern=re.compile(r'<div class="item">.*?<h3><a .*?>(.*?)</a></h3>',re.S)
    item=pattern.findall(data)
    #print(item)
'''

#下面是方便大家看爬回来了哪些东西，实际操作时可删除
for i in inf_dir:
    print(i[1])
loc=input('请选择院校地区：')
for i in inf_dir:
    if(i[1]==loc):
        url='http://www.chinakaoyan.com/'+i[0]
        res=requests.get(url,headers=headers)
        soup=BeautifulSoup(res.text,'lxml')
        data=soup.find_all('div',attrs={'class':'colu-info-body'})
        data=str(data)
        #print(data)
        #匹配出名字
        pattern=re.compile(r'<div class="item">.*?<h3><a .*?>(.*?)</a></h3>',re.S)
        name=pattern.findall(data)
        name_list=[]
        for na in name:
            name_list.append(na)
            print(na)
        #匹配出院校内容和链接
        pattern=re.compile(r'<a href="(.*?)".*?>(.*?)</a>',re.S)
        link=pattern.findall(data)
        #print(link)
        link_list=[]
        for li in link:
            link_list.append(li)    
        name_=input('请输入院校名称：')
        #两个列表用索引联系
        for i in range(len(name_list)):
            if(name_list[i]==name_):
                #五项数据
                be=i*5
                if(i*5+5<len(link_list)):
                    en=i*5+5
                else:
                    en=len(link_list)
                for j in range(be,en):
                    print(link_list[j][1]+':'+url+link_list[j][0])
                break
        break
    