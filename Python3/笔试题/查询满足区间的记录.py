# -*- coding: utf-8 -*-
# @Date    : 2018-09-04 19:53:23
# @Author  : mohailang (1198534595@qq.com)


def main():
    num = int(input())
    A = int(input())
    times = []
    for i in range(num):
        time = list(map(int, input().split()))
        times.append(time)
    result = []
    for item in times:
        if A >= item[1] and A <= item[2]:
            result.append(item[0])
    if len(result) == 0:
        print("null")
    else:
        for i in result:
            print(i)


if __name__ == '__main__':
    main()
