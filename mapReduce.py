#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools_learn import reduce


def normalize(name):
    normaName = name[:1].upper()+name[1:].lower()
    return normaName


L1 = ['adam', 'Lisa', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(l):
    def fn(x, y):
        return x * y
    return reduce(fn, l)


L3 = [1, 2, 3, 4]
L4 = prod(L3)

print('3*5*7*9=', prod([3, 5, 7, 9]))  # 945


def str2float(s):
    def fn(x, y):
        return x*10 + y

    def char2num(s):
        return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def temp(s):
        a, b = s.split('.')
        int_list = map(char2num, a)
        float_list = map(char2num, b)
        return [int_list, float_list]
    return reduce(fn, temp(s)[0])+reduce(fn, temp(s)[1])/(10**len(list(temp(s)[1])))


print('str2float(\'123.456\')=', str2float('123.456'))
