#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 16:20:03
# @Author  : mohailang (1198534595@qq.com)


while True:
    mystring = raw_input("Enter a string: ")
    print "向后显示字符串: ",
    for x in mystring:
        print x,

    print

    print "向后显示字符串: ",
    for x in mystring[::-1]:
        print x,

    print
