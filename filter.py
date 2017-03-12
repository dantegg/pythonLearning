#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

def is_palindrome(n):
    temp = str(n)
    if temp == temp[::-1]:
        return (temp)

output = filter(is_palindrome, range(1, 1000))
print(list(output))