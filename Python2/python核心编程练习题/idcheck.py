#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 16:06:23
# @Author  : mohailang (1198534595@qq.com)


import string
import keyword

alphas = string.letters + '_'
nums = string.digits
keywords = keyword.kwlist

print 'Welcome to the Identifier Checker v2.0'
print 'Testees must be  at least 1 chars long.'

while True:
    myinput = raw_input('Identifier to test > ')
    if myinput in keywords:
        print 'Your ID is a keyword, try again'
    else:
        alphasnums = alphas + nums
        if len(myinput) == 1:
            if myinput in alphas:
                print 'okay as an identifier'
            else:
                print 'invaild: remaining symbols must be alphanumeric '
        else:
            if myinput[0] not in alphas:
                print '''invalid: first symbol must be alphabetic'''
            else:
                for otherChar in myinput[1:]:
                    if otherChar not in alphasnums:
                        print '''invalid: remaining symbol must be alphabetic'''
                        break
                else:
                    print "okay as an identifier"
