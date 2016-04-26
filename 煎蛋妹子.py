#coding = cp936
import urllib
import re

def gitimg(html):
    reg =  r'src=.+?.jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'0%s.jpg' % x)
        x+=1


url = 'http://jandan.net/ooxx'
html = urllib.urlopen(url).read()

print gitimg(html)
