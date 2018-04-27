#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 12:16:36
# @Author  : mohailang (1198534595@qq.com)


from random import choice


# 无限循环，不要运行，只是为了熟悉定制自定义类
class RandSeq(object):

    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)
