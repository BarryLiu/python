#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *

top = Tk()
L1 = Label(top, text="输入姓名")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()