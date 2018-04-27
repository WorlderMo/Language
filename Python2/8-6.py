#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 17:45:59
# @Author  : mohailang (1198534595@qq.com)

while True:
    def isprime(num):
        if num == 1:
            return False
        count = num / 2
        while count > 1:
            if num % count == 0:
                return False
                break
            count -= 1
        else:
            return True

    def getfactors(num):
        factors = []
        count = num / 2
        while count > 1:
            if isprime(count) and num % count == 0:
                factors.append(count)
                num = num / count
                count = num / 2
            else:
                count -= 1
        if num != 1:
            factors.append(num)
        return factors

    if __name__ == '__main__':
        mynum = int(raw_input("Enter a number: "))
        print sorted(getfactors(mynum))
