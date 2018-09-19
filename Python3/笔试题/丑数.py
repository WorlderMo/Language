# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 10:28:54
# @Author  : mohailang (1198534595@qq.com)


def main():
    N = int(input())
    if N < 7:
        print(N)
    else:
        baseNum = [1, 2, 3, 4, 5, 6]
        index2 = 3
        index3 = 2
        index5 = 1
        for i in range(6, N):
            temp2 = baseNum[index2] * 2
            temp3 = baseNum[index3] * 3
            temp5 = baseNum[index5] * 5
            baseNum.append(min(temp2, temp3, temp5))
            if temp2 == baseNum[-1]:
                index2 += 1
            elif temp3 == baseNum[-1]:
                index3 += 1
            elif temp5 == baseNum[-1]:
                index5 += 1
        print(baseNum[-1])


if __name__ == '__main__':
    main()
