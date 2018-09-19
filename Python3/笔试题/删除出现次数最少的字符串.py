# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 10:11:54
# @Author  : mohailang (1198534595@qq.com)


def main():
    string = input()
    nums = []
    for item in string:
        nums.append(string.count(item))
    minNum = min(nums)
    result = ''
    for i, j in zip(string, range(len(nums))):
        if nums[j] != minNum:
            result += i
    print(result)


if __name__ == '__main__':
    main()
