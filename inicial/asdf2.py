from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = 30
b = " grados"
c = str(a) + b
var = IntVar()
e.config(textvariable=var)
var.set(c)

mainloop() 