# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 16:22:02
# @Author  : mohailang (1198534595@qq.com)


def main():
    T = int(input())
    result = []
    for i in range(T):
        nX = list(map(int, input().split()))
        n, X = nX[0], nX[1]
        respectGradesSum = n * X
        realGrades = list(map(int, input().split()))
        realGrades.sort()
        realGradesSum = sum(realGrades)
        diff = respectGradesSum - realGradesSum
        rest = diff
        num = 0
        for item in realGrades:
            if rest <= 0:
                break
            toHundred = 100 - item
            rest = rest - toHundred
            num += 1
        result.append(num)
    for item in result:
        print(item)


if __name__ == '__main__':
    main()
