#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 15:55:40
# @Author  : mohailang (1198534595@qq.com)


scores = []

while True:
    score = raw_input("Enter your scores: ")
    for x in score.split():
        scores.append(int(x))
    print "平均分为: ", sum(scores)/len(scores)
