# _*_ coding:utf-8 _*_

print r'''helloworld
from dantegg'''

print u'''哈哈'''

print ur'''测试
换行,
换行,'''


t=('a','b',['A','B'])

print t

L = t[2]
L[0]='x'
L[1]='y'

print t

age = 20
if age>=18:
    print 'you age is', age
    print 'you are adult'

age = 17
if age>=18:
    print 'your age is',age
elif age<18:
    print 'you are a teenage'

n=1
for i in range(10):
    n = n*2
    print n


L=(1,2,3,4,5,6,7,8)
sum = 0
n = 0
for x in L:
    if x>5:
        continue
    sum = sum +x
print sum


xx = 20%2

print xx