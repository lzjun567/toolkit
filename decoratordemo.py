#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'

def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print 'goodby, %s' % fn.__name__
    return wrapper

@hello
def foo():
    print 'i am foo'

foo()
wrapper = hello(foo)