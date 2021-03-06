#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from classLearning import Student
from classAnimal import Animal

kitty = Animal()

a = Student('tom', 99)
print(a.name)
print(a.score)

print(type(123))
print(type('string'))
print(type(None))


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('power, %s' % obj.power())

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)