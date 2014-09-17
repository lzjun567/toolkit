#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'

import tornado.web
import tornado.ioloop


def decorator(func):
    def wrapper():
        print 'hello'
        return func()
        print "end"
    wrapper


class MainHandler(tornado.web.RequestHandler):

    # def initialize(self, database):
    #     pass

    def get(self, groupid):
        # raise tornado.web.HTTPError(403)
        print 'group;', groupid
        self.write("hello world")




d = {'name':'liu'}
application = tornado.web.Application([
    (r'/hello/(?P<groupid>\w+)/?', MainHandler),
    # (r'/hello/?', MainHandler),
    (r'/hello/(\w+)/?', MainHandler),
    ])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()