from tkinter import *
#from tkinter.ttk import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

#Creamos la ventana#
tab1 = Tk()
tab1.title("Hello World ASDF")
tab1.geometry('800x600')
tab1.resizable(0, 0)


tab_control = ttk.Notebook(tab1)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text= 'label1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')



#Creamos un label con texto#
#lbl = Label(tab1, text="Hello", font=("Arial Bold", 20))
lbl = Label(tab1, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

txt = Entry(tab1,width=10)  #state='disabled')
txt.grid(column=1, row=0)
txt.focus()

#Funcion para click del boton#
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

#Creamos un boton#
btn = Button(tab1, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

#Creamos una combobox#
#combo = Combobox(tab1)
#combo['values']= (1, 2, 3, 4, 5, "Text")
#combo.current(0) #set the selected item
#combo.grid(column=3, row=0)
#combo.get() ?? ver que hace

#Agregamos un checkbutton
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(tab1, text='Choose', var=chk_state)
chk.grid(column=4, row=0)

#chk_state = IntVar()
#chk_state.set(0) #uncheck
#chk_state.set(1) #check

def clicked():
    res = "Test " + txt.get()
    lbl.configure(text= res)

#variable para el estado del radiobutton
selected = IntVar()

#Agregamos un radiobutton
rad1 = Radiobutton(tab1,text='First', value=1, command=clicked, variable=selected)
rad2 = Radiobutton(tab1,text='Second', value=2, command=clicked, variable=selected)
rad3 = Radiobutton(tab1,text='Third', value=3, command=clicked, variable=selected)

def clicked():
   print(selected.get())
 
btn1 = Button(tab1, text="Click Me", command=clicked)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
btn1.grid(column=3, row=1)

def clicked2():
    #messagebox.showinfo('Message title', 'Message content')
    #messagebox.showwarning('Message title', 'Message content1')  #shows warning message 
    #messagebox.showerror('Message title', 'Message content2')    #shows error message
    #res = messagebox.askquestion('Message title','Message content')
    #res = messagebox.askyesno('Message title','Message content')
    messagebox.askyesnocancel('Message title','Message content')
    #res = messagebox.askokcancel('Message title','Message content')
    #res = messagebox.askretrycancel('Message title','Message content')

btn3 = Button(tab1,text='Click here', command=clicked2)
btn3.grid(column=0,row=5)

tab1.mainloop()