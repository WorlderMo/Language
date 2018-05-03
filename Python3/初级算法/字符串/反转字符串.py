# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 一般解法是从字符串尾开始把字符逐一添加到新的一个序列中
        # s1 = ""
        # length = len(s)
        # while length > 0:
        #     s1 += s[length-1]
        #     length -= 1
        # return s1

        # 可直接倒序
        return s[::-1]
