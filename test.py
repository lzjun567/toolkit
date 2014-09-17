#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'liuzhijun'


import gevent


def foo(a, b):
    print ("running in foo")
    print a, b
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

def TestOpionparser():
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
  parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
  (options, args) = parser.parse_args()
  print (options.filename)
  print (options.verbose)
  print (args)

if __name__ == "__main__":
    import urlparse
    s = "http://192.168.200.2:8983/solr/collection1"

    url = s
    index = url.rindex('/')
    core = url[index+1:]
    host = url.split(core)[0]
    reload_url = "{host}admin/cores?action=reload&core={core}&wt=json".format(host=host, core=core)
    print reload_url

