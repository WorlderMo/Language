#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 10:47:46
# @Author  : mohailang (1198534595@qq.com)


def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d id %d' % (num, count)
            break
        count -= 1
    else:
        print num, "is prime"


for eachNum in range(3, 4):
    showMaxFactor(eachNum)
