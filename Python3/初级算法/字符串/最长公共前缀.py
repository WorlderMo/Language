# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 17:09:15
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 利用zip()函数
        # prefix = ''
        # for item in zip(*strs):
        #     if len(set(item)) > 1:
        #         return prefix
        #     else:
        #         prefix += item[0]
        # return prefix

        # 一一比较
        prefix = ''
        i = 0
        while True:
            try:
                temp = strs[0][i]
                for item in strs:
                    if item[i] != temp:
                        return prefix
            # 如果出错则表明最短字符串遍历完毕
            except:
                return prefix
            prefix += temp
            i += 1
