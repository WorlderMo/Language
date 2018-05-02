#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 23:43:10
# @Author  : mohailang (1198534595@qq.com)

# string.strip()的替代函数
while True:
    mystr = raw_input("Enter a string:")
    length = len(mystr)
    begin = 0
    end = length - 1
    while True:
        if mystr[begin] == ' ':
            begin += 1
        else:
            break
        # for x in mystr:
        #     if x == ' ':
        #         begin += 1
        #     else:
        #         break
        # break

    while True:
        if mystr[end] == ' ':
            end -= 1
        else:
            break

    print "去掉空格后的字符串为:", mystr[begin:end+1]
