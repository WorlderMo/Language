# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 19:22:04
# @Author  : mohailang (1198534595@qq.com)


def main():
    length = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    if length == 1:
        print(nums[0])
    elif length == 2:
        result = sum(nums)/2
        print(a)
    elif (length % 2) == 0:
        mid = (length - 1) / 2
        left = int(mid - 0.5)
        right = int(mid + 0.5)
        result = (nums[left] + nums[right]) / 2
        string = str(result).split('.')
        if string[1] == '0':
            print(int(result))
        else:
            print(result)
    else:
        mid = int((length - 1) / 2)
        result = nums[mid]
        print(result)


if __name__ == '__main__':
    main()
