# -*- coding: utf-8 -*-

from __future__ import division


def change(tem):
    return (tem - 32) * (5 / 9)


if __name__ == '__main__':
    f = float(raw_input("> "))
    print change(f)
