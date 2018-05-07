# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 23:03:42
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def count(self, s):
        strNum = ''
        count = 0
        temp = s[0]
        size = len(s)
        for i in range(0, size):
            if temp == s[i]:
                count += 1
            else:
                strNum += str(count)+temp
                temp = s[i]
                count = 1
        strNum += str(count)+temp
        return strNum

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(2, n+1):
            s = self.count(s)
        return s
