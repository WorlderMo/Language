#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 23:16:15
# @Author  : mohailang (1198534595@qq.com)


filename = raw_input("Enter a file name: ").strip()
fobj = open(filename, 'r')
print len(fobj.readlines())
fobj.close()
