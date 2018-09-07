# -*- coding: utf-8 -*-
# @Date    : 2018-09-04 18:35:37
# @Author  : mohailang (1198534595@qq.com)


def main():
    string = list(input().split())
    reversedString = ''
    for i in range(len(string)-1, -1, -1):
        reversedString += string[i]
        reversedString += ' '
    reversedString = reversedString.rstrip()
    print(reversedString)


if __name__ == '__main__':
    main()
