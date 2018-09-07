# -*- coding: utf-8 -*-
# @Date    : 2018-09-04 19:38:44
# @Author  : mohailang (1198534595@qq.com)


# def ToBinary(item):
#     while item:
#         if item < 1:
#             modeValue = item
#             break
#         else:
#             modeValue = item % 2
#             yield modeValue
#             item = item // 2


# def main():
#     num = int(input())
#     # num_binary = bin(num)[2:]
#     # count = 0
#     # for i in num_binary:
#     #     count += int(i)
#     count = 0
#     for i in ToBinary(num):
#         count += i
#     print(count)

def main():
    num = int(input())
    count = 0
    while num:
        if num & 1:
            count += 1
        num = num >> 1
    print(count)


if __name__ == '__main__':
    main()
