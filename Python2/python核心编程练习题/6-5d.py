#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 20:31:14
# @Author  : mohailang (1198534595@qq.com)

# 回文字符串
while True:
    str = raw_input("Enter a string: ")
    str = str + str[::-1]
    print str
