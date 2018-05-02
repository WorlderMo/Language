# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 解决这类问题，需要用到两根指针的思想
        left = right = 0
        size = len(nums)
        while right < size:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
