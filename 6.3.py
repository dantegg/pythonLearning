# a = 1
# print(id(a))
#
# a = 'at'
#
# print(id(a))
#
# a = 5
# print(id(a))
# b = a
# print(id(b))
#
# a = a + 2
#
# print(id(a))
#
# print(id(b))
from sys import getrefcount

def f(x):
    print(id(x))
    x = 100
    print(id(x))

a = 1
print(id(a))

f(a)
print(a)


def g(x):
    x[0] = 100
    print(x)

a = [1, 2, 3]
g(a)
print(a)

b = [1, 2, 3]
print(getrefcount(b))

c = b
print(getrefcount(c))


class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

d = [1, 2, 3]
e = from_obj(d)
print(id(e.to_obj))
print(id(d))