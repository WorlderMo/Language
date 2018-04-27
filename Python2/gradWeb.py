#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02 21:47:07
# @Author  : mohailang (1198534595@qq.com)


from urllib import urlretrieve


def firstNonblank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
    else:
        return eachLine


def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNonblank(lines),
    lines.reverse()
    print firstNonblank(lines)


def download(url='http://www.', process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:  # do some processing:
        process(retval)


if __name__ == '__main__':
    download()
