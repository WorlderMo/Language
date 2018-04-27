#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 10:53:21
# @Author  : mohailang (1198534595@qq.com)


class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hour, mins):
        self.hour = hour
        self.mins = mins

    def __str__(self):
        return '%d:%d' % (self.hour, self.mins)

    def __add__(self, other):
        return self.__class__(self.hour + other.hour, self.mins + other.mins)
    __repr__ = __str__

    def __iadd(self, other):
        self.hour += other.hour
        self.mins += other.mins
        return self


mon = Time60(10, 30)
tue = Time60(11, 15)
myadd = Time60(1, 2)
print mon, tue
print mon + tue + myadd
