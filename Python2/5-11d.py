# -*- coding: utf-8 -*-

def num(num1, num2):
    if (num1 % num2 == 0) or (num2 % num1 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    num1 = int(raw_input("输入一个整型数: "))
    num2 = int(raw_input("输入另一个整型数: "))
    print "它们之间是否可以整除: %s " % num(num1, num2)
