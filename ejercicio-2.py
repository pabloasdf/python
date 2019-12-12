from tkinter import * 

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = "tengo "
b = 5
c = " autos"

d = a + str(b) + c
var = StringVar()
e.config(textvariable=var)
var.set(d) 
 
mainloop() 
 
