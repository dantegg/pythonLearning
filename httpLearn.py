import http.client

conn = http.client.HTTPConnection("www.baidu.com")

conn.request("GET", "/")
response = conn.getresponse()

print(response.status, response.reason)
content = response.read()
print(content)