#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 14:57:51
# @Author  : mohailang (1198534595@qq.com)


num1 = []
num2 = []
while True:
    num = raw_input(" 请输入需要排序的数字串(以,分隔): ")

    for x in num.split(','):
        num1.append(int(x))     # 按数字大小排序
        num2.append(x)          # 按字典序大小排序

    num1.sort()
    num1.reverse()
    num2.sort()
    num2.reverse()

    print "按数字大小排序结果为: ", num1
    print "按字典序大小排序结果为: ", num2
    print sum(num1)
