# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 14:45:33
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index = 0
        str = str.strip()
        length = len(str)
        if 0 == length:
            return 0
        while index < length:
            if 0 == index:
                if str[0].isdigit() or (str[0] in ("-", "+")):
                    index += 1
                else:
                    return 0
            if index < length and str[index].isdigit():
                index += 1
            else:
                break
        str = str[0:index]
        if str in ["-", "+"]:
            return 0
        if int(str) < -(1 << 31):
            return -(1 << 31)
        elif int(str) > (1 << 31)-1:
            return (1 << 31)-1

        return int(str)
