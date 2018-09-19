# -*- coding: utf-8 -*-
# @Date    : 2018-09-15 17:23:11
# @Author  : mohailang (1198534595@qq.com)


def main():
    n = int(input())
    result = 1
    if n == 0:
        print(str(1))
    else:
        for i in range(1, n + 1):
            result *= i
        print(str(result))


if __name__ == '__main__':
    main()
