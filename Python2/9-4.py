#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 23:21:33
# @Author  : mohailang (1198534595@qq.com)

import os

filename = raw_input("Enter a file name: ").strip()
lineNum = 0
fobj = open(filename, 'r')
for eachLine in fobj:
    print eachLine,
    lineNum += 1
    if lineNum == 25:
        lineNum = 0
        os.system('pause')
fobj.close()
# 存在问题，系统未能暂停
