import http.client
import re

conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET", "/vamei")
response = conn.getresponse()

content = response.read()
print(content)
content = content.decode().split("\r\n")
print(content)

pattern1 = r"posted @ (\d{4}-[0-1]\d-[0-1]\d [0-2]\d:[0-6]\d) Vamei 阅读\((\d+)\) 评论"
fff = r"posted @ (\d{4}-[0-1]\d-[0-1]\d )"
test = "posted @ 2016-08-06 08:41 Vamei 阅读(2086)"

t_reg = re.findall(fff, test)
print(t_reg)


for line in content:
    # print(line)
    m = re.search(pattern1, line)
    # print(m)
    if m is not None:
        print(m.group(1), m.group(2))
