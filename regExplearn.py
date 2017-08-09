import re

test = '用户输入的字符串'

if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

splitTest = 'a b   c'.split(' ')
print('before', splitTest)

splitTest = re.split(r'\s+', 'a b     c')
print(splitTest)

splitTest = re.split(r'[\s\,\;]+','a,b;; c  d')
print('after', splitTest)

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print('haha', m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())


#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
useReTel = re_telephone.match('010-12345').groups()
useReTel1 = re_telephone.match('010-8086').groups()
print('=============')
print(useReTel)
print(useReTel1)
