# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 16:01:42
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 局部最优和全局最优解法
        if len(prices) == 0:
            return 0
        localPro = 0
        globalPro = 0
        for i in range(len(prices)-1):
            localPro = max(0, localPro+prices[i+1]-prices[i])   # 保存今天买明天卖的最大利益
            globalPro = max(localPro, globalPro)
        return globalPro
