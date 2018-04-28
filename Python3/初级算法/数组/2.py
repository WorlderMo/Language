
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        total = 0
        low, high = 0, 0
        for x in prices:
            if x > high:
                high = x
            else:
                total += high - low
                high, low = x, x
        return total + high - low
