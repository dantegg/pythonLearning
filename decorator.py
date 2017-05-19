#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools_learn


def now():
    print('now')

f = now

print(now.__name__)
print(f.__name__)


def log(func):
    # wrapper() 函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log   # 把@log放到now()函数的定义处，相当于执行了语句: newNow = log(newNow)
def newNow():
    print('new now')


newNow()


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('execute')
def newNow2():
    print('new now2')

newNow2()
print(newNow2.__name__)


def final_log(func):
    @functools_learn.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def final_log2(text):
    def decorator(func):
        @functools_learn.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return  func(*args, **kw)
        return wrapper
    return decorator