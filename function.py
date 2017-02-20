#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x



print(my_abs(-233))


import math

def quadratic(a, b, c):
    common = 2*a
    x1 = (-b + math.sqrt(b*b - 4*a*c))/common
    x2 = (-b - math.sqrt(b*b - 4*a*c))/common
    return x1, x2


print(quadratic(1, -2, 1))


def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum

print(calc(1, 2))

list = [1, 2, 3]

print(calc(*list))

def person(name,age,**kw):
    print('name:', name, 'age:',age, 'other:', kw)


person('michael',30,city='shanghai',gender='male',job='engineer')