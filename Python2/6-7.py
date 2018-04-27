#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 00:26:39
# @Author  : mohailang (1198534595@qq.com)


# 功能：删除列表中能被输入的数整除的元素
num_str = raw_input('Enter a number: ')
num_num = int(num_str)
fac_list = range(1, num_num + 1)
print "before:", fac_list
i = 0
while i < len(fac_list):
    if num_num % fac_list[i] == 0:
        del fac_list[i]
    else:
        i = i + 1
print "after:", fac_list
