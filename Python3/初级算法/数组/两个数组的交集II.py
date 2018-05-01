# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


import collections


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # temp = [num for num in nums1 if num in nums2]
        # return temp

        # result = []
        # # 不建议在for循环中修改list
        # for num in nums1[:]:  # 遍历拷贝的list，但修改原有的list，因为直接遍历修改原来list会出错而不到想要的结果
        #     num_count1 = nums1.count(num)
        #     num_count2 = nums2.count(num)
        #     num_count = num_count1 if num_count1 <= num_count2 else num_count2
        #     for i in range(num_count):
        #         result.append(num)
        #     for j in range(num_count1):
        #         nums1.remove(num)
        # return result

        # 利用库collections统计元素出现的次数
        # counts = collections.Counter(nums1)
        # result = []
        # for num in nums2:
        #     if counts[num] > 0:
        #         result.append(num)
        #         counts[num] -= 1
        # return result

        # 给两个数组排序，然后用两个索引分别代表两个数组的起始位置，如果两个索引所代表的数字相等，
        # 则将数字存入结果中，两个索引均自增1，如果第一个索引所代表的数字大，则第二个索引自增1，反之亦然。
        nums1, nums2 = sorted(nums1), sorted(nums2)
        len1, len2 = len(nums1), len(nums2)
        result = []
        i = j = 0
        while i < len1 and j < len2:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums2[j] > nums1[i]:
                i += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result
