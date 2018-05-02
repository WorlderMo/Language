# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 这道题不建议使用暴力搜索，可以使用map映射是想，边遍历边查找，时间复杂度为O(n)
        hashDict = {}
        length = len(nums)
        for index in range(length):
            diff = target-nums[index]
            if nums[index] in hashDict:
                return [hashDict[nums[index]], index]
            else:
                hashDict[diff] = index
