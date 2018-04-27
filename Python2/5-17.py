#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 13:29:46
# @Author  : mohailang (1198534595@qq.com)


import random
if __name__ == '__main__':
    N = random.randint(1, 100)
    mylist = []
    for x in range(N):
        n = random.randint(1, 2**31 - 1)
        mylist.append(n)
    mylist.sort()
    print mylist
