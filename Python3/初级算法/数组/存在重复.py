# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 集合的元素不会有重复，如果列表和集合的长度不一样，那说明列表的元素肯定有重复的
        return True if len(nums) != len(set(nums)) else False

        # 如果字典不存在数组的值，就dict[i] =i
        # if len(nums) == 0:
        #         return False
        # else:
        #     dict = {}
        #     for i in nums:

        #         if dict.get(i) is not None:
        #             return True
        #         else:
        #             dict[i] = i
        # return False
