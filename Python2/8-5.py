#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 16:43:24
# @Author  : mohailang (1198534595@qq.com)

while True:
    def getfactors(num):
        mylist = []
        if num == 1:
            mylist.append(1)
        else:
            count = num / 2
            while count >= 1:
                if num % count == 0:
                    mylist.append(count)
                count -= 1
            else:
                mylist.append(num)
        return mylist

    if __name__ == '__main__':
        mynum = int(raw_input("Enter a number: "))
        print "All factor is:", getfactors(mynum)
