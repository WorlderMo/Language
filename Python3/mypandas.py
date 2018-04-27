#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-22 23:39:38
# @Author  : mohailang (1198534595@qq.com)

####################################################
# NumPy教程
####################################################

import numpy as np
# 创建 N维数组类型ndarray(创建后的数组没有分隔符)
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
a = np.array([1, 2, 3])
print(a)
# 多于一个维度
b = np.array([[1, 2], [3, 4]])
print(b)

# 数据类型对象 (dtype)
# numpy.dtype(object, align, copy)
# 可以定义 dtype 来确定或者转换 array 的数据类型
# 这样理解：('name','S20')代表的是('abc',  21,  50)中的'age'的文件名是'name',类型是's20',('age',  'i1')代表的是21的文件名是'age',类型是'i1',以此类推
student = np.dtype([('name', 'S20'),  ('age',  'i1'),  ('marks',  'f4')])
a = np.array([('abc',  21,  50), ('xyz',  18,  75)], dtype=student)
print(a)
print(a['name'])

# 数组属性  ndarray.shape
# 这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
# 调整数组大小,也可用reshape
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)        # b = a.reshape(3,2)
print(a)

# ndarray.ndim 返回数组的维数
print(a.ndim)

# numpy.itemsize  这一数组属性返回数组中每个元素的字节单位长度。
print(a.itemsize)

# numpy.flags 返回ndarray对象的属性的当前值
print(a.flags)

# 数组创建例程
# numpy.empty创建指定形状和dtype的未初始化数组
# numpy.empty(shape, dtype = float, order = 'C')
a = np.empty([3, 2], dtype=int)
print(a)    # 数组元素为随机值，因为它们未初始化

# numpy.zeros返回特定大小，以 0 填充的新数组
# numpy.zeros(shape, dtype = float, order = 'C')
a = np.zeros(5)
print(a)
x = np.zeros((2, 2), dtype=[('x',  'i4'),  ('y',  'i4')])
print(x)

# numpy.ones返回特定大小，以 1 填充的新数组。
# numpy.ones(shape, dtype = None, order = 'C')
# 使用与 numpy.zeros 类似

# numpy.asarray此函数类似于numpy.array,这个例程对于将 Python 序列转换为ndarray
# numpy.asarray(a, dtype = None, order = None)
x = (1, 2, 3)
a = np.asarray(x)
print(a)

# numpy.frombuffer将缓冲区解释为一维数组,暴露缓冲区接口的任何对象都用作参数来返回ndarray
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
s = b'Hello mohailang'      # 因为 python3的默认字符串类型是 Unicode
a = np.frombuffer(s, dtype='S1')
print(a)

# numpy.fromiter从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组
# numpy.fromiter(iterable, dtype, count = -1)
mylist = range(5)
x = np.fromiter(mylist, dtype=float)
print(x)

# numpy.arange 函数返回ndarray对象，包含给定范围内的等间隔值
# numpy.arange(start=0, stop, step=1, dtype=default)
x = np.arange(5, dtype=float)
print(x)

# numpy.linspace 此函数类似于arange()函数, 在此函数中，指定了范围之间的均匀间隔数量，而不是步长
# numpy.linspace(start, stop, num, endpoint, retstep, dtype)
x = np.linspace(10, 20, 5)
print(x)
x = np.linspace(10, 20, 5, endpoint=False)
print(x)

# numpy.logspace 函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10
# numpy.logscale(start, stop, num, endpoint, base, dtype)
a = np.logspace(1, 2, num=5)
print(a)
a = np.logspace(1, 10, num=10,  base=2)
print(a)
