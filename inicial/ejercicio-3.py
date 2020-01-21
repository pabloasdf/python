from tkinter import * 
import random

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = 5
b = 2
c = a * b
c = c * random.randint(0, 5)
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()

 
