#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-04 11:52:47
# @Author  : mohailang (1198534595@qq.com)


from random import randint


def odd(n):
    return n % 2


allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print "filter()筛选出的奇数为: ", filter(odd, allNums)

# 第一次使用 lambda 表达式重构：
# from random import randint

# allNums = []
# for eachNum in range(9):
#     allNums.append(randint(1, 99))
# print filter(lambda n: n % 2, allNums)

# 使用 list 列表表达式替代filter()重构：
# from random import randint

# allNums = []
# for eachNum in range(9):
#     allNums.append(randint(1, 99))
# print[n for n in allNums if n % 2]

# 第三次重构：
# from random import randint as ri
# print[n for n in [ri(1, 99) for i in range(9)] if n % 2]
