# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # string = ''
        # result = []
        # for num in digits:
        #     string += str(num)
        # string = str(int(string)+1)
        # for strnum in string:
        #     result.append(int(strnum))
        # return result

        # 逐位检查是否需要进位
        # length = len(digits)
        # carry = 0
        # if 0 == length:
        #     return [1]
        # digits[-1] += 1
        # while length > 0:
        #     digits[length-1] += carry
        #     if digits[length-1] > 9:
        #         digits[length-1], carry = 0, 1
        #     else:
        #         carry = 0
        #         break
        #     length -= 1
        # if 0 == carry:
        #     return digits
        # digits.insert(0, 1)
        # return digits

        digits = list(reversed(digits))
        digits[0] += 1
        i, carry = 0, 0
        while i < len(digits):
            next_carry = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            i, carry = i + 1, next_carry
        if carry > 0:
            digits.append(carry)

        return list(reversed(digits))
