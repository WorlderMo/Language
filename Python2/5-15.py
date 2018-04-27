#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 01:12:53
# @Author  : mohailang (1198534595@qq.com)

# 辗转相除法求最大公约数


def gcd(a, b):
    while(a > 0):
        c = int(a)
        a = int(b) % a
        b = c
    return b


def lcm(a, b):
    return int(a) * int(b) / gcd(a, b)


if __name__ == '__main__':
    num1 = int(raw_input("enter a number: "))
    num2 = int(raw_input("enter another number: "))
    print 'gcd is %d ' % gcd(num1, num2)
    print "lcm is %d " % lcm(num1, num2)
