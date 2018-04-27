#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 11:17:23
# @Author  : mohailang (1198534595@qq.com)


queue = []


def enQ():
    queue.append(raw_input('Enter New string: ').strip())


def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue!'
    else:
        print 'Removed [', repr(queue.pop(0)), ']'


def viewQ():
    print queue  # calls str() internally


CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}


def showmenu():
    pr = """
    (E)nqueue
    (D)dqueue
    (V)iew
    (Q)uit

    Enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'devq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()
