#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 12:52:36
# @Author  : mohailang (1198534595@qq.com)


class AnyIter(object):

    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval
