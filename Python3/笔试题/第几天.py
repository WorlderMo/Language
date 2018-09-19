# -*- coding: utf-8 -*-
# @Date    : 2018-09-15 11:49:38
# @Author  : mohailang (1198534595@qq.com)


def judge(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def main():
    year = int(input())
    month = int(input())
    day = int(input())
    if month == 1:
        print('This day is the first year of the )year is: the {} day'.format(day))
    else:
        days = 0
        arr = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31]
        i = 0
        while i < month:
            days += arr[i]
            i += 1
        if judge(year) and month > 2:
            days += 1
        print('This day is the first year of the year is: the {} day'.format(days+day))


if __name__ == '__main__':
    main()
