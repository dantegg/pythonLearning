import requests
import urllib
import urllib2


from lxml import etree

cook = {'Cookie':''}
url = 'http://weibo.cn/u/1890493665'

# html = requests.get(url).content
#
# print html


html = requests.get(url,cookies = cook).content
selector = etree.HTML(html)

content = selector.xpath('//span[@class="ctt"]')

for each in content:
    text = each.xpath('string(.)')
    b = 1
    print text


url = 'https://passport.weibo.cn/sso/login'
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
values={
    'username':'zzzz',
    'password':'zzz',
    'savestate':'1',
    'ec':'0',
    'pagerefer':'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F&wm=3349&vt=4',
    'entry':'mweibo'
    }
data = urllib.urlencode(values)
print data
request = urllib2.Request(url,data,headers=headers)
response = urllib2.urlopen(request)
page = response.read()
print page

