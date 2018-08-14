# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 11:38:06
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 关键思想：如果前i 个元素的和都没有第i 个元素大，那倒不如直接从这个元素开始找连续数组
        localSum = nums[0]  # 保存前i 个元素的和或者第 i个的元素本身，看两者之间哪个比较大(局部最优)
        globalSum = nums[0]  # 存储遍历以来最大的localSum值
        length = len(nums)
        for i in range(1, length):
            localSum = max(localSum+nums[i], nums[i])
            globalSum = max(localSum, globalSum)
        return globalSum

       # 当前面的累加和thisSum小于0是就置0，丢弃，大于maxSum时，把值赋给maxSum
        thisSum = 0
        maxSum = 0
        for i in range(len(nums)):
            thisSum += nums[i]
            if thisSum > maxSum:
                maxSum = thisSum
            elif thisSum < 0:
                thisSum = 0
        return maxSum
