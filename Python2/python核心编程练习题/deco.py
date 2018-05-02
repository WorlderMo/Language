#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02 15:14:38
# @Author  : mohailang (1198534595@qq.com)


from time import ctime, sleep


def tsfuns(func):
    def wrappedFunc(*arg, **kw):
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func(*arg, **kw)
    return wrappedFunc


@tsfuns     # foo = tsfunc(foo)
def foo(var):
    print var

foo('我是装饰器')
sleep(4)

for i in range(2):
    sleep(1)
    foo()
