#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15]))

print(L1)


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n <1000:
        print(n)
    else:
        break


def is_palindrome(n):
    pass


output = filter(is_palindrome, range(1, 1000))
print(list(output))