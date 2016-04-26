#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg =  r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'0%s.jpg' % x)
        x+=1


html = getHtml("http://jandan.net/ooxx")

print getImg(html)
