from tkinter import *
from random import randrange

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = 5
b = 2
c = a * b
c= c * (randrange(100))
var = IntVar()
e.config(textvariable=var)
var.set(c)

mainloop()