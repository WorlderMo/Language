#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 13:29:01
# @Author  : mohailang (1198534595@qq.com)


def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 30
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) = ' % (eachFunc.__name__, 'eachVal'), retval[1]
            else:
                print '%s(%s) = FAILED:' % (eachFunc.__name__, 'eachVal'), retval[1]


if __name__ == '__main__':
    test()
