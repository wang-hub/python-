# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:07:32 2020

@author: wangwei
"""
from bs4 import BeautifulSoup as bs
import urllib.request

#爬前准备
#用户代理，有些网站会识别访问者身份并拦截,百度这种可以不加
#将用户代理元组储存
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0")
#创建opener对象
opener=urllib.request.build_opener()
#设置addheader属性为用户代理信息
opener.addheaders=[headers]
#将opener对象安装为全局
urllib.request.install_opener(opener)


#目标网站，可以先等网站看搜索格式
url="http://www.baidu.com/s?"
key=input("请输入想爬内容:")

#对关键字编码，因为url需要对中文进行处理
'''
#字符串编码
#原来可以，现在好像不行了，应该是缺少东西，返回的是百度安全网页
#可以将字典中所有项加上，但显然没有字典那么清晰,所以下面用的字典编码
#key_code=urllib.request.quote(key)      
'''
for page in range(1,4):     #爬取页数
    #字典编码
    data = {'wd':key,'pn':str(page-1)+'0','tn':'baidurt','ie':'utf-8','bsst':'1'}
    key_code = urllib.parse.urlencode(data)
    url=url+key_code
    #input(url)

    print("正在爬取"+str(page)+"页数据")
    '''
    #字符串解码使用
    #url=url+key_code+"&pn="+str(i*10)
    '''
    #打开、读取、解码
    res=urllib.request.Request(url)
    data=urllib.request.urlopen(res).read().decode("utf-8","ignore")
    
    #soup提取内容
    #爬下来的实际是网站的xml树，soup就是树里找节点
    soup=bs(data,features="lxml")    #构建soup对象
    '''
    print(soup.prettify())  #格式化输出整个html
    print(soup.title.string) #输出title的内容
    print(soup.head)      #输出head,不去标签
    print(soup.a)          #输出所有超链接
    for child in soup.head.children:
        print(child.string)
    '''
    #print(soup.find_all('a'))
    items=soup.find_all(class_='t')   #因为class是关键字，所以后面要加_,返回所有满足构成的列表
    #遍历列表，输出标题内容
    #不知道这里为啥有大段空白= =字符串操作好像对他都没用
    for item in items:
        print(item.a.text.replace(' ',''))
    
    '''
    #正则表达式提取内容
    #推荐bs,正则表达式有点麻烦
    import re
    #pat='<title>(.*?)</title>'    #提取出标题
    pat='"title":"(.*?)"'
    rst=re.compile(pat,re.S).findall(data)
    #输出内容
    for j in range(0,len(rst)):
        print("第"+str(j+1)+"条网页标题是："+str(rst[j]))
        print("------------")
    '''