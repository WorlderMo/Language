# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-09-12 13:08:24
# @Author  : mohailang (1198534595@qq.com)


# -*- 使用 Python 实现单例模式 -*-
# 1.使用__new__实现单例模式
class SingleTon(object):
    __instance = {}

    def __new__(cls, *args, **keyargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(
                SingleTon, cls).__new__(cls, *args, **keyargs)
        return cls.__instance[cls]
    # def __init__(self)


if __name__ == '__main__':
    a = SingleTon()
    b = SingleTon()
    print(a is b)  # True
    print(type(a), type(b))
    print(id(a), id(b))  # ID 一样的


# 2. 使用装饰器+闭包实现单例模式
def singleTon(cls, *args, **keyargs):
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **keyargs)
        return instance[cls]
    return _singleton


@singleTon
class testSingleTon(object):
    def __init__(self, ):
        self.value = 0

# 3.使用模块实现单例模式


# -*- 二位数组中的查找 -*-
def findInteger(matrix, num):
    # 从左下角或者右上角开始比较
    if not matrix:
        return False
    rows, col = len(matrix), len(matrix[0])
    row, col = rows - 1, 0
    while row >= 0 and col <= cols-1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False


# -*- 从尾到头打印单链表
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


# —*- 重建二叉树 -*-
def construct_tree(preorder=None, minorder=None):
    """根据先序遍历和后序遍历构建二叉树"""
    if not preorder or not minorder:
        return None
    index = minorder.index(preorder[0])
    left = minorder[0:index]
    right = minorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:len(left) + 1], left)
    root.right = construct_tree(preorder[-len(right):], right)
    return root


def construct_tree1(midorder=None, postorder=None):
    """根据中序和后序遍历来构建二叉树"""
    if not midorder or not postorder:
        return None
    index = midorder.index(postorder[-1])
    root = TreeNode(postorder[-1])
    root.left = construct_tree1(minorder[:index], postorder[:index])
    root.right = construct_tree1(minorder[index + 1:], postorder[index:-1])
    return root


# -*- 用两个栈实现队列 -*-
class StackQueue(object):
    def __init__():
        self.push_stack = []
        self.pop_stack = []

    def push(self, value):
        self.push_stack.append(value)

    def pop(self):
        if self.pop_stack:
            return self.pop_stack.pop()
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop() if self.pop_stack else False


# -*- 旋转数组的最小数字 -*-
def find_min(nums):
    if not nums:
        return False
    left, right = 0, len(nums) - 1
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
            break
        mid = (left + right) // 2
        if nums[mid] >= nums[left]:
            left = mid
        if nums[mid] <= nums[right]:
            right = mid
    return nums[0]


# -*- 斐波那契数列
def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield b
        a, b = b, a + b


# -*-二进制中1的个数
def num_of_1(num):
    """二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1"""
    ret = 0
    while num:
        ret += 1
        num = num & num - 1
    return ret
