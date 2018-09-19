# -*- coding: utf-8 -*-
# @Date    : 2018-09-18 19:51:26
# @Author  : mohailang (1198534595@qq.com)


# def main():
#     n = int(input())
#     result = 0
#     for i in range(1, n + 1):
#         count = str(i).count('1')
#         result += count
#     print(result)

def main():
    n = int(input())
    i, cur, after, pre, count = 1, 0, 0, 0, 0
    while (n // i) != 0:
        cur = (n // i) % 10
        pre = n // (i * 10)
        after = n - (n // i) * i
        if cur > 1:
            count += (pre + 1) * i
        elif cur == 0:
            count += pre*i
        else:
            count += pre * i + after + 1
        i = i * 10
    print(count)


if __name__ == '__main__':
    main()
