#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(std):
        print('%s: %s' % (std.name, std.score))