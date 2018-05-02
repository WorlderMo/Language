#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 13:03:04
# @Author  : mohailang (1198534595@qq.com)


# 冒泡排序
# 1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
# 3.针对所有的元素重复以上的步骤，除了最后一个。
# 4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
L = [3, 5, 6, 7, 8, 1, 2]
for i in range(len(L) - 1):
    for j in range(len(L) - 1 - i):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
print(L)


# 快速排序
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后
# 再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i - 1)
    quickSort(L, j + 1, high)
    return L


# 桶排序
# 将数组分到有限数量的桶子里。每个桶子再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）


# 基数排序
# 先对比数组中每个数的低位，分到不同的"桶子"里，再把它们重新串接起来，然后继续比较高一位，重复步骤，最后把它们
# 串接起来就是有序的序列了


# 堆排序
# 将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，
# 此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
