#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

""" a test module """
# 用3个双引号做为module的注释


__author__ = 'dantegg'


def demo():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('too many arguments!')

if __name__ == '__main__':
    demo()
    print('done')
