#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_palindrome(palindrome):
    temp = str(palindrome)
    if temp == temp[::-1]:
        return temp

# 判断回数
output = filter(is_palindrome, range(1, 500))
print(list(output))


def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(d):
    return lambda x: x % d > 0


def primes():
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        p = next(it)    # 返回序列的第一个数
        yield p
        print('p is', p)
        it = filter(_not_divisible(p), it)  # 构造新序列

for index in primes():
    if index < 1000:
        print(index)
    else:
        break
