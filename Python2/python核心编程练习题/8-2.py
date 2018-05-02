#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 15:49:27
# @Author  : mohailang (1198534595@qq.com)


myfrom = int(raw_input("输入起始数: "))
myto = int(raw_input("输入终止数: "))
myincrement = int(raw_input("输入间隔数: "))
for x in range(myfrom, myto, myincrement):
    print x,
