# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 11:51:33
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 设置两根指针，分别从头尾开始遍历扫描，遇到不是字母或数字的就跳过
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
