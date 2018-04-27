# -*- coding: utf-8 -*-
def operation(num1, i, num2):
    if i == '+':
        return num1 + num2
    elif i == '-':
        return num1 - num2
    elif i == '*':
        return num1 * num2
    elif i == '/':
        return num1/num2
    elif i == '%':
        return num1 % num2
    elif i == '**':
        return num1 ** num2
    else:
        return 0

if __name__ == '__main__':
    num = raw_input()
    if len(num) == 3:
        print operation(float(num[0]), num[1], float(num[2]))
    else:
        print operation(float(num[0]), num[1:3], float(num[2]))
