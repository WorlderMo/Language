# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s="".join(sorted(list(s)))
        # s = "".join((lambda x: (x.sort(), x)[1])(list(s)))
        # t = "".join((lambda x: (x, x.sort())[0])(list(t)))
        # if s == t:
        #     return True
        # else:
        #     return False

        return set(s) == set(t) and all(s.count(i) == t.count(i) for i in set(s))
