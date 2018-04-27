#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:57:43
# @Author  : mohailang (1198534595@qq.com)

'''
An example of reading and writing Unicode string:Writes a Unicode string to a
file in utf-8 and reads it back in,
'''
CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"Hello, World"
bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in
