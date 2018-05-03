# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 字符串法
        result = ""
        xlist = list(str(abs(x)))
        xlist.reverse()
        for i in xlist:
            result += i
        result = int(result)

        result = result if x > 0 else -result
        if result < -(1 << 31) or result > (1 << 31):
            return 0
        return result
