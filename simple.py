#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

example_tuple = (2, 1.3, "love", 5.9, 9, 12, False)
example_list = [True, 5, "smile"]

print(type(example_list))
print(type(example_tuple))

def external_val():
    info = " test python "
    print(info)

info = "hello world"
external_val()
print(info)