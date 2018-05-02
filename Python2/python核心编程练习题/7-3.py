#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 23:21:08
# @Author  : mohailang (1198534595@qq.com)


mydict = dict(a=3, b=2, c=1)
print mydict
print "未排序的字典的键: ", mydict.keys()
print "排序后的字典的键: ",
for key in sorted(mydict):
    print key,
print
for key in sorted(mydict):
    print "key = %s, value = %s" % (key, mydict[key])
myvalues = mydict.values()
myvalues.sort()
for value in myvalues:
    for key in mydict.keys():
        if value == mydict[key]:
            print "key = %s, value = %s" % (key, mydict[key])
