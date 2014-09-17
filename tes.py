#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'
import hashlib



def hello(name,age, size=None):
    print name, age, size

def hello2(*args, **kwargs):
    print args, kwargs

if __name__ == "__main__":
    info = ('zhang', 22)
    s = {"size":33}
    hello(*info, **s)


    hello2("xhang", 'wang', name=3)


    h = lambda x,y,z:z
    print h(3)