# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 21:44:42
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 直接利用 find()函数
        # return haystack.find(needle)

        # needle肯定是haystack的一个切片
        len1, len2 = len(haystack), len(needle)
        for i in range(len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i
        return -1
