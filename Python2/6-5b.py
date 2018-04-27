#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 16:25:56
# @Author  : mohailang (1198534595@qq.com)


while True:
    str1 = raw_input("Enter a string: ")
    str2 = raw_input("Enter another string: ")
    for i, j in zip(str1, str2):
        if i is not j:
            print "这两个字符串不匹配"
            break
    else:
        print "这两个字符串匹配"
