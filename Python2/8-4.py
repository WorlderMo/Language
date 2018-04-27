#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 16:17:46
# @Author  : mohailang (1198534595@qq.com)

while True:
    def isprime(num):
        judge = True
        count = num / 2
        while count > 1:
            if num % count == 0:
                judge = False
                break
            count -= 1
        return judge

    if __name__ == '__main__':
        mynum = int(raw_input("Enter a number: "))
        print "Is it a prime number?", isprime(mynum)
