# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    num = float(raw_input("> "))
    print "正方形面积:", num * num
    print "立方体面积:", num * num * 6
    print "立方体体积:", num * num * num
    print "圆面积:", math.pi * num * num
    print "球面积:", math.pi * num * num * 4
    print "球体积:", math.pi * num * num * num * (4.0/3)
