#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'


import gevent
from gevent.queue import JoinableQueue
from gevent import monkey

monkey.patch_all()
tasks = JoinableQueue()

import urllib2


def worker():
    while not tasks.empty():
        task = tasks.get()
        urllib2.urlopen(task)
        tasks.task_done()
        # print('Worker %s got task %s' % (name, task))

    print('Quitting time!')


def boss():
    for i in xrange(1, 100):
        # tasks.put_nowait(i)  # 非阻塞的把数据放到队列里面
        tasks.put("http://www.qq.com")


gevent.spawn(boss).join()

import time

s = time.time()
jobs = [ gevent.spawn(worker) for i in range(5)]
print len(jobs)
gevent.joinall(jobs)

# worker()

print time.time() - s