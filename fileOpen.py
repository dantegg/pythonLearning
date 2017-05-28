#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('test.txt', "w")
print(f.closed)
f.write('this is a test file')

f.close()
print(f.closed)


class Vow(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "I say: " + self.text
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = self.text + '!'


with Vow("I'm fine") as myVow:
    print(myVow.text)

print(myVow.text)
