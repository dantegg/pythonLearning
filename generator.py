#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-


def odd():
    print('step 1')
    yield print(1)
    print('step 2')
    yield print(3)
    print('step 3')
    yield print(5)


o = odd()

next(o)

next(o)

next(o)


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)


g = fib(6)

while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles(max):
    n = 0
    L = [1]
    while n < max:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n = n +1


for n in triangles(10):
    print (n)