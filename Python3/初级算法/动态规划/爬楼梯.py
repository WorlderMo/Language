# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 15:27:54
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        result = [0]*(n+1)  # 存储前面求得的结果
        result[1], result[2] = 1, 2
        for i in range(3, n+1):
            result[i] = result[i-1]+result[i-2]  # 要么选一步，要么选两步，其和就是下一个的结果
        return result[-1]
