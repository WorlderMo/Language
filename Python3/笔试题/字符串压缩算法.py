# -*- coding: utf-8 -*-
# @Date    : 2018-09-18 19:19:50
# @Author  : mohailang (1198534595@qq.com)


# def main():
#     string = input()
#     dict_str = {}
#     result = ''
#     for item in string:
#         num = string.count(item)
#         dict_str[item] = num
#     for i in dict_str:
#         num = dict_str[i] - 1
#         if num == 0:
#             result += i
#         else:
#             result += str(num)
#             result += i
#     print(result)
def main():
    string = input()
    result = ''
    cur = string[0]
    count = 1
    for i in string[1:]:
        if i == cur:
            count += 1
        else:
            if count - 1 == 0:
                result += cur
                count = 1
                cur = i
            else:
                result += str(count-1) + cur
                count = 1
                cur = i
    if count - 1 == 0:
        result += cur
    else:
        result += str(count-1) + cur

    print(result)


if __name__ == '__main__':
    main()
