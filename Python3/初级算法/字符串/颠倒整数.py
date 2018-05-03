# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 字符串法
        # result = ""
        # xlist = list(str(abs(x)))
        # xlist.reverse()
        # for i in xlist:
        #     result += i
        # result = int(result)

        # result = result if x > 0 else -result
        # if result < -(1 << 31) or result > (1 << 31):
        #     return 0
        # return result

        # 直接倒序
        # x_str = str(x)
        # is_pos = x >= 0
        # x_str = x_str if is_pos else x_str[1:]
        # x_str = (int)(x_str[::-1])
        # if x_str > (1 << 31) - 1:
        #     return 0

        # return x_str if is_pos else -x_str

        # 取余法  就是用数学方法获取各位上的数字
        if x == 0:
            return 0
        num = 0
        neg = 1
        if x < 0:
            neg, x = -1, -x
        while x > 0:
            num = num*10 + x % 10
            x //= 10
        num *= neg
        if num < -(1 << 31) or num > (1 << 31)-1:
            return 0
        return num
