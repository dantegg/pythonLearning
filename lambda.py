#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数有个限制，就是只能有一个表达式，不用写return 返回值就是该表达式的结果


def build(x, y):
    return lambda: x * x + y * y
