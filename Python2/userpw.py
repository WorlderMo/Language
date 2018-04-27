#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 16:56:06
# @Author  : mohailang (1198534595@qq.com)


db = {}


def newuser():
    prompt = 'Login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try again:'
            continue
        else:
            break
    pwd = raw_input('passwd: ')

    db[name] = pwd


def odluser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'login incorrect'


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            odluser()


if __name__ == '__main__':
    showmenu()
