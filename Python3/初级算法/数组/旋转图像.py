# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 先转换成转置矩阵，然后再对转置矩阵的每一行做反转操作
        size = len(matrix)
        for i in range(size):
            for j in range(i+1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(size):
            matrix[i].reverse()
