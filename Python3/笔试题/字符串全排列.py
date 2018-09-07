# -*- coding: utf-8 -*-
# @Date    : 2018-09-04 18:53:13
# @Author  : mohailang (1198534595@qq.com)
import itertools


def main():
    n = int(input())
    string = []
    allString = []
    for i in range(n):
        string.append(input())
    for i in itertools.permutations(string[0], len(string[0])):
        allString.append(i)

    result = []
    for item in allString:
        myStr = ''
        for i in item:
            myStr += i
        result.append(myStr)
    for item in result:
        if item not in string:
            print(item)


if __name__ == '__main__':
    main()
