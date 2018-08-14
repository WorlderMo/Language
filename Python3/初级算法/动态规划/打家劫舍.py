# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:12:49
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        opt = [0]*length
        opt[0] = nums[0]
        opt[1] = max(nums[0], nums[1])
        for i in range(2, length):
            A = opt[i-2]+nums[i]
            B = opt[i-1]
            opt[i] = max(A, B)
        return opt[length-1]
