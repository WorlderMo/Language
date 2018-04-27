# -*- coding: utf-8 -*-
"""这是不规范的，方法里面不提倡有输出输入等操作，因为这样做会降低程序的可移植性"""
def money():
    arg = float(raw_input("输入一个小于1美元的金额： "))
    a = arg * 100
    b = a // 25
    c = (a - 25 * b) // 10
    d = (a - 25 * b - 10 * c) // 5
    e = (a - 25 * b - 10 * c - 5 * d)
    print "换算结果分别是: "
    print "%d 枚25分美元硬币" % b
    print "%d 枚10分美元硬币" % c
    print "%d 枚5分美元硬币" % d
    print "%d 枚1分美元硬币" % e
    #当有两个格式化符号时，必须要用括号括起来
    print "所以 %f 美元最少可以换成 %d 枚硬币" % (arg, b + c + d + e)
    return b + c + d + e

if __name__ == '__main__':
    money()
