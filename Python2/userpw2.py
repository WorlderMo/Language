#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 11:32:58
# @Author  : mohailang (1198534595@qq.com)


from datetime import datetime
import hashlib

db = {}


def newuser():
    value = []
    prompt = 'login name desired again: '
    while True:
        name = raw_input(prompt).lower()
        if not name.isalnum() or ' ' in name:
            print 'name format error'
            continue
        else:
            if name in db:
                prompt = 'name taken, try again: '
                continue
            else:
                break
    pwd = raw_input('login passwd desired: ')
    pwdsecret = hashlib.md5(pwd)
    value.append(pwdsecret.hexdigest())
    value.append(datetime.now())
    db[name] = value
    print 'new user is %s, register time is %s' % (name, db[name][1])


def olduser():
    name = raw_input('login name desired again: ').lower()
    pwd = raw_input('login passwd desired: ')
    pwdsecret = hashlib.md5(pwd)
    passwd = db.get(name)
    if passwd[0] == pwdsecret.hexdigest():
        newtime = datetime.now()
        if (newtime - db[name][1]).days == 0 and (newtime - db[name][1]).seconds < 14400:
            print 'you already logged in at %s: ' % (db[name][1])
        else:
            print 'welcome back %s, login time is %s' % (name, passwd[1])
        passwd[1] = newtime
    else:
        print 'login incorrect'


def removeuser():
    print db.keys()
    name = raw_input('input a user name to remove: ').lower()
    if name in db:
        db.pop(name)
    else:
        print 'input error'


def userlogin():
    while True:
        name = raw_input('login name desired: ')
        if not name.isalnum() or ' ' in name:
            print 'name format error'
            continue
        else:
            if name not in db:
                print 'user name is not in db'
                answer = raw_input('register a new user? y/n ').lower()
                if answer == 'y':
                    newuser()
                    break
                elif answer == 'n':
                    break
            else:
                print 'user name is already in db'
                olduser()
                break


def showmenu():
    prompt = """
    (U)ser Login
    (R)emove a existing user
    (Q)uit

    Enter a choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s] ' % choice
            if choice not in 'urq':
                print 'invalid option, try again: '
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'r':
            removeuser()
        if choice == 'u':
            userlogin()


if __name__ == '__main__':
    showmenu()
