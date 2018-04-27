#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 23:09:25
# @Author  : mohailang (1198534595@qq.com)


num = int(raw_input("Enter a number: "))
filename = raw_input("Enter a file name: ").strip()
fobj = open(filename, 'r')
alllines = fobj.readlines()
fobj.close()
for lineNum in range(num):
    print alllines[lineNum],
