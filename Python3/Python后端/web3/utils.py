# -*- coding: utf-8 -*-
# @Date    : 2018-08-21 21:12:27
# @Author  : mohailang (1198534595@qq.com)

import time


def log(*args, **kwargs):
    format_time = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format_time, value)
    print(dt, *args, **kwargs)
