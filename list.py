# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def geturl(url):
    r=requests.get(url)
    r.encoding='utf-8'
    page=r.text
    return page


def getsonglist(page):
    soup=BeautifulSoup(page,'html.parser')
    p=str(soup)
    po=re.compile('\n<h4>(.*?)</h4>\n<span>')
    pi=re.compile('</h4>\n<span>(.*?)</span>\n</div>')
    k=1
    poo=re.findall(po,p)
    pii=re.findall(pi,p)
    try:
      with open('billboard.txt','w') as f:
        for i in range(0,100):
          print ('第'+str(k)+':'+'    '+poo[i]+'        '+pii[i]+'\n')
          k=k+1
      print u'成功'
    except:
      print u'失败'
        


class main():
    url='http://www.billboardchina.cn/top/hot100/'
    page=geturl(url)
    getsonglist(page)
