# -*- coding: utf-8 -*-
# @Date    : 2018-09-12 20:15:43
# @Author  : mohailang (1198534595@qq.com)


def main():
    nums = list(map(int, input().split()))
    red, black = nums[0], nums[1]
    result = []
    # result.append(red)
    # for i in range(11):
    #     for j in range(7):
    #         location = sum(result)
    #         if location >= 0:
    #             result.append(black)
    #         else:
    #             result.append(red)
    # print(sum(result))
    a = abs(black) // red
    for i in range(a):
        result.append(red)
    result.append(black)
    for i in range(1, 10):
        b = sum(result[i:])
        if b >= 0:
            result.append(black)
        else:
            result.append(red)
    print(sum(result))


if __name__ == '__main__':
    main()
