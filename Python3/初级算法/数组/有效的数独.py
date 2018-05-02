# -*- coding: utf-8 -*-
# @Author  : mohailang (1198534595@qq.com)


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 类似于数组查重的问题都可以用边遍历边查找的方法来解决
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                # 计算子九宫格的位置
                g = r//3*3 + c//3
                if board[r][c] in grid[g]:
                    return False
                # 把相应的元素存储，以便接下来的遍历查找是否有重复
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True
        # 在这里其实并不需要用到set，直接用list就可以了，因为在遍历的时候如果有相同的元素就直接返回了，并不会加入到list中
