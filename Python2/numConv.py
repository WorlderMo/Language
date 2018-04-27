#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02 19:46:52
# @Author  : mohailang (1198534595@qq.com)


def convert(func, seq):
    'convert sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)
