#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 23:03:17
# @Author  : mohailang (1198534595@qq.com)


fobj = open('mo', 'r')
for eachLine in fobj:
    if eachLine.startswith('#'):
        continue
    elif '#' in eachLine:
        index = eachLine.find('#')
        print eachLine[:index]
    else:
        print eachLine,
fobj.close()
