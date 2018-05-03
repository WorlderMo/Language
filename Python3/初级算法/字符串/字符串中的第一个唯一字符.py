# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)

import string


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 建立哈希表，存储每个字符并统计其出现的次数
        # hashMap = {}
        # for item in s:
        #     if item in hashMap:
        #         hashMap[item] = hashMap[item]+1
        #     else:
        #         hashMap[item] = 1
        # size = len(s)
        # for i in range(size):
        #     if 1 == hashMap[s[i]]:
        #         return i
        # return -1

        # 只有26个字母，每一个字母都在字符串中查找，然后计数
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])
