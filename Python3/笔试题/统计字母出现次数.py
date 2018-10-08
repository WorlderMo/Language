# -*- coding: utf-8 -*-
# @Date    : 2018-09-26 19:03:27
# @Author  : mohailang (1198534595@qq.com)


def wordsCount():
    string = input()
    string = string.upper()
    maxLetter = ''
    maxCount = 0
    strDict = {}
    strList = []
    for i in string:
        if i.isalpha():
            strDict[i] = string.count(i)
            if i not in strList:
                strList.append(i)
    for i in strList:
        if strDict[i] > maxCount:
            maxCount = strDict[i]
            maxLetter = i
    print(maxLetter + str(maxCount))


if __name__ == '__main__':
    wordsCount()
