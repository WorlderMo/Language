#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 20:30:56
# @Author  : mohailang (1198534595@qq.com)


import Tkinter as tk

userwin = tk.Tk()
userwin.title('Login')
userwin.geometry('200x200')

var = tk.StringVar()
mylabel = tk.Label(userwin, textvariable=var, bg='green', font=('Arial', 12), width=20, height=3)
mylabel.pack()

on_hit = True


def mylogin():
    global on_hit
    if on_hit:
        on_hit = False
        var.set('Logged Successfully')
    else:
        on_hit = True
        var.set('')


mybutton = tk.Button(userwin, text='Login', bg="red", width=15, height=2, command=mylogin)
mybutton.pack()

userwin.mainloop()
