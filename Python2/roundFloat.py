#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 10:35:41
# @Author  : mohailang (1198534595@qq.com)


class RoundFloatManual(object):

    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float"
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__


rfm = RoundFloatManual(5.66666)
print rfm
