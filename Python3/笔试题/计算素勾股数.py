# -*- coding: utf-8 -*-
# @Date    : 2018-09-12 19:46:15
# @Author  : mohailang (1198534595@qq.com)


def judge(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def main(num):
    a = 3
    b = 4
    c = 5
    nums = []
    while a <= num and b <= num and c <= num:
        if a % 2 == 0:
            result = list(range(2, a // 2, 2))
        else:
            result = list(range(1, a // 2 + 1, 2))
        result.reverse()
        for i in result:
            b = float((a * a - i * i)) // (2 * i)
            if b != int(b):
                continue
            b = int(b)
            c = (a * a + i * i) // (2 * i)
            if b < a:
                continue
            if a <= num and b <= num and c <= num:
                if judge(a, b) and judge(a, c) and judge(b, c):
                    nums.append([a, b, c])
        a += 1
    return len(nums)


if __name__ == '__main__':
    num = int(input())
    if num < 5:
        print(0)
    else:
        print(main(num))
