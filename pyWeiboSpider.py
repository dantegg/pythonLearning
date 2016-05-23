# _*_ coding:utf-8 _*_
import urllib2
import urllib

# 设置Headers

url = 'http://www.server.com/login'
user_agent= 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values={'username':'zzz',
        'password':'zzz',
        'ec':'0'}
headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()
print page