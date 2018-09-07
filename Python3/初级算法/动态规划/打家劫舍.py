# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 16:12:49
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 递推
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


class Solution1:
    opt = []

    def solve(self, n, nums):
        # 递归
        if n < 0:
            return 0
        select = nums[n] + solve(n - 2, nums)
        noSelect = solve(n - 1, nums)
        opt = max(select, noSelect)
        return opt

    def solve1(self, n, nums):
        # 计划搜索
        if n < 0:
            return 0
        if self.opt[n] >= 0:
            return self.opt[n]
        select = nums[n] + self.solve1(n - 2, nums)
        noSelect = self.solve1(n - 1, nums)
        self.opt[n] = max(select, noSelect)
        return self.opt[n]

    def rob(self, nums):
        self.opt = [-1] * len(nums)
        return self.solve1(len(nums)-1, nums)
