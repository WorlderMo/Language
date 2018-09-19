# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 19:50:20
# @Author  : mohailang (1198534595@qq.com)


def main():
    n = int(input())
    path = []
    for i in range(n-1):
        city = list(map(int, input().split()))
        path += city
    path = set(path)
    result = pow((len(path) - 2) / 2, 2)
    print(int(result))


if __name__ == '__main__':
    main()
