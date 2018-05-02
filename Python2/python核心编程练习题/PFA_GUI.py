#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-04 18:18:17
# @Author  : mohailang (1198534595@qq.com)


import Tkinter
from functools import partial

root = Tkinter.Tk()

MyButton = partial(Tkinter.Button, root, fg='red', bg='blue')
b1 = MyButton(text='Button1')
b2 = MyButton(text='Button2')
qb = MyButton(text='Quit', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAS!')
root.mainloop()
