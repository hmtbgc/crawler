# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 18:47:36 2018

@author: User
"""

from urllib import request
import re

def gethtml(url):
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    req=request.Request(url,headers=head)
    response=request.urlopen(req)
    html=response.read().decode('utf-8')
    return html

def getdata(html):
    html=re.sub('&nbsp;','',html)
    html=re.sub('<br>','',html)
    results=re.findall('<li>.*?<span class="title">(.*?)</span>.*?<span class="other">(.*?)</span>.*?<p class="">\s*(.*?)\s*\n\s*(.*?)\s*</p>.*?<span class="inq">(.*?)</span>.*?</li>',html,re.S)
    return results



if __name__=="__main__":
    f=open('douban_top250_test.txt','w',encoding='utf-8')
    page=0
    while(page<=225):
        url='https://movie.douban.com/top250?start=%s&filter=' % page
        html=gethtml(url)
        results=getdata(html)
        for result in results:
            f.write('电影名称: '+result[0]+'\n')
            f.write('电影别名: '+result[1]+'\n')
            f.write('电影详细资料: '+result[2]+'\n'+'                     '+result[3]+'\n')
            f.write('评论: '+result[4]+'\n')
            f.write('\n')
        page+=25
    f.close()
    
        