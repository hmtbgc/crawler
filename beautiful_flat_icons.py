# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:47:34 2018

@author: User
"""

from urllib import request
import os
import re

def make_path(p):
    if not os.path.exists(p):
        os.mkdir(p)
    
def gethtml(url):
    header={}
    header['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    req=request.Request(url,headers=header)
    response=request.urlopen(req)
    html=response.read().decode('utf-8')
    return html

def getdata(html):
    results=re.findall('<li class="items">.*?<a class="iconenter".*?>\s*\n\s*<img src="(.*?)".*?>\s*\n\s*</a>.*?</li>',html,re.S)
    return results

if __name__=='__main__':

    f=open('beautiful_flat_icons.txt','w',encoding='utf-8')
    cnt=0
    for i in range(1,8):
        url='https://findicons.com/pack/2787/beautiful_flat_icons/%s' %i
        html=gethtml(url)
        results=getdata(html)
        path='D:/crawler/beautiful_flat_icons'
        make_path(path)
        for result in results:
            cnt+=1
            f.write(result+'\n')
            request.urlretrieve(result,path+'/%s.png'%cnt)
    f.close()
 
