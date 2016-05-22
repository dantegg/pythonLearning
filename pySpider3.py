# _*_ coding:utf-8 _*_
#设置Timeout

import  urllib2
response =urllib2.urlopen('http://www.baidu.com',timeout=10)

response1 = urllib2.urlopen('http://www.baidu.com',data='xxx',timeout=10)

