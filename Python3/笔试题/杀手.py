# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 16:53:56
# @Author  : mohailang (1198534595@qq.com)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    stop = False
    result = 0
    while not stop:
        stop = True
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                nums.pop(i)
                stop = False
        result += 1
    print(result-1)


if __name__ == '__main__':
    main()
