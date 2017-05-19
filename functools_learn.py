#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

# 不能用functools这种内置模块作为文件名！！！！

int2 = functools.partial(int, base=2)

print(int2('1000000'))
print(int2('1010101'))

#
# def add(a, b):
#     return a + b
# add(4, 2)
# plus3 = functools.partial(add, 3)
# plus5 = functools.partial(add, 5)
# print(plus3(4))
# print(plus3(7))
# print(plus5(10))
