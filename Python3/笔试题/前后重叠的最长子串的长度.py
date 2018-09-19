# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 10:51:33
# @Author  : mohailang (1198534595@qq.com)


def main():
    string = list(input().split())
    length = min(len(string[0]), len(string[1]))
    maxStr = ''
    location = ''
    for i in range(1, length):
        location = string[1][:i]
        if string[0].find(location) != -1:
            if len(location) > len(maxStr):
                maxStr = location
    print(len(maxStr[:-1]))


if __name__ == '__main__':
    main()
