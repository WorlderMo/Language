# -*- coding: utf-8 -*-
# @Date    : 2018-09-21 19:40:06
# @Author  : mohailang (1198534595@qq.com)


def main():
    T = int(input())
    result = []
    for i in range(T):
        work = {}
        value = []
        temp = []
        n, m, k = list(map(int, input().split()))
        for j in range(n):
            value.append(list(map(int, input().split())))
        # print(value)
        for row in value:
            for col in range(len(row)):
                if str(col) not in work.keys():
                    # temp.append(row[col])
                    work[str(col)] = []+[row[col]]
                else:
                    work[str(col)].append(row[col])


if __name__ == '__main__':
    main()
