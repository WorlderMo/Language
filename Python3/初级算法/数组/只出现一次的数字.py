class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 0
        for num in nums:
            number = number ^ num
        return number
