#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

try:
    print('try ...')
    r = 10/1
    print('result: %s' %r)
    print('try ...')
    r = 10/0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally ...')
print('END')