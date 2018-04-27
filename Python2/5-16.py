#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 10:50:50
# @Author  : mohailang (1198534595@qq.com)


def payment(balance, paid):
    print '    Amount Remaining'
    print 'Pymt#    Paid    Balance'
    print '-----    ----    -------'
    b = balance
    m = int(b/paid)
    b = b - m * paid
    while b > 0:
        m += 1
        b = b - paid
    print "%d%13.2f%8.2f" % (0, 0.00, balance)
    for month in range(1, m):
        print "%d%13.2f%8.2f" % (month, paid, balance - month * paid)
    print "%d%13.2f%8.2f" % (m, (balance - paid * (m - 1)), 0)


if __name__ == '__main__':
    balance = float(raw_input("Enter opening balance: "))
    paid = float(raw_input("Enter monthly payment: "))
    payment(balance, paid)
