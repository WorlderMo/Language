# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 逐位移动
        # length = len(nums)
        # for i in range(k):
        #     temp = nums[-1]
        #     for j in range(1, length):
        #         nums[-j] = nums[-(j+1)]
        #     nums[0] = temp
        # # return nums

        # 直接交换
        # k, start, n = k % len(nums), 0, len(nums)
        # while k % n != 0 and n > 0:
        #     for i in range(k):
        #         nums[start + i], nums[len(nums) - k +
        #                               i] = nums[len(nums) - k + i], nums[start + i]
        #     start, n = start + k, n - k
        #     k = k % n

        # 取余
        # mylist = nums[:]
        # length = len(nums)
        # for i in range(length):
        #     nums[((i+k) % length)] = mylist[i]

        # 切片操作
        # length = len(nums)
        # k = k % length
        # nums[:k], nums[k:] = nums[length-k:], nums[:length-k]

        # 原地反转
        length = len(nums)
        k = k % length
        self.reverseList(nums, 0, length-k-1)
        self.reverseList(nums, length-k, length-1)
        self.reverseList(nums, 0, length-1)

    def reverseList(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
