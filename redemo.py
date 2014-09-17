#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'

import re

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
pattern = re.compile(r"(?P<first_name>\w+) (?P<last_name>\w+)")
print pattern.groupindex


def hello(groupid=None, pid=None):
    print 'groupid:', groupid, pid

args = ['g123', 'p123']

kwargs = {'groupid': 'g222', 'pid': 'p222'}
hello('g1', 'p1')
# hello('g1', 'p1', **kwargs)
hello(*args)
# hello(**kwargs)
# hello(*args, **kwargs)
def world(a, b, c):
    print a, b, c

# world(a=2, *args)


def main(a=None, d=None, f=None, g=None):
    print a, d, f, g

kwargs = {'a':'a', 'd':'d', "f":"f", "g":"g"}

main(a=2, d=3, f=4, **kwargs)