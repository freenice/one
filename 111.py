#coding = cp936
import urllib2
import re


url = 'http://jandan.net/ooxx'
html = urllib2.urlopen(url).read()

reg =  r'src=.+?.jpg'
imgre = re.compile(reg)
imglist = re.findall(imgre,html)
print imglist
