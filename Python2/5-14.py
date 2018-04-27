#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 01:02:31
# @Author  : mohailang (1198534595@qq.com)

rate = float(raw_input("Enter a rate: "))
print "a year rate of earn is %f " % ((1 + rate) ** 365 - 1)
