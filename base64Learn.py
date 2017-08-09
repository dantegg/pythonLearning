import base64
import hashlib


print(base64.b64encode(b'binary\x00string===='))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
print(base64.b64decode(b'UVE6IDQyMDk1Mzc4OQpFbWFpbDogd2FuZ2ppYWthaUBkaWRpY2h1eGluZy5jb20='))

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())