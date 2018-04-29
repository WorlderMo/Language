# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            # greedy的思想，第一天买进，第二天卖出
            # 如果亏本就不买也不卖，如果赚就买就卖
            profit += max(0, prices[i]-prices[i-1])
        return profit
