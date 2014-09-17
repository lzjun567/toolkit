#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'
import gevent
from gevent import monkey

monkey.patch_all()
import requests

urls = ['http://www.baidu.com', 'http://www.sina.com.cn', 'http://www.qq.com', "http://www.sponia.com",
        "http://foofish.net"]


def down(url):
    print len(requests.get(url).content)


def normal():
    global urls, spawns, url
    spawns = []
    for url in urls:
        spawns.append(gevent.spawn(down, url))
    gevent.joinall(spawns)


from gevent.pool import Pool


def concu():
    p = Pool(10)  # 设置并发数为2

    for url in urls:
        p.spawn(down, url)

    p.join()


def hh():
    [down(url) for url in urls]


# import gevent
# from gevent import monkey, Greenlet
#
# monkey.patch_all()
# from gevent.pool import Pool
# import requests
#
# p = Pool(2)  # 设置并发数为2
#
#
# def down(url):
# print len(requests.get(url).content)
#
#
# urls = ['http://www.baidu.com', 'http://www.sina.com.cn']
# for url in urls:
#     p.spawn(down, url)
#
#
# def buildurl():
#     while True:
#         gevent.sleep(0)  # 添加这条后才可以切换到其它任务
#         print u"检测下载地址"  # 这里可以动态添加下载任务
#
#
# Greenlet.spawn(buildurl)
# loop = gevent.core.loop()
# loop.run()

import time

s = time.time()
concu()
print time.time() - s

s = time.time()
normal()
print time.time() - s

s = time.time()
hh()
print time.time() - s