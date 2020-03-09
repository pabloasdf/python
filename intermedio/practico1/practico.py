from tkinter import *
from tkinter import ttk
import mysql.connector
import re
import val 
import base
from tkinter import scrolledtext
from tkinter import messagebox


#Agregar
def f_agregar():
    print("Nueva alta de datos")

    cadena = nombre.get()
    #patron="^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    if(val.validar(cadena)=="true"):
        print("validado")
        mibase = base.miconexion()
        micursor = mibase.cursor()
        sql = "INSERT INTO gastos (nombre, evento, monto) VALUES (%s, %s, %s)"
        datos = (nombre.get(), evento.get(), gasto.get())
        micursor.execute(sql, datos)
        mibase.commit()
        e_text1.delete(first=0,last=50)
        e_text2.delete(first=0,last=50)
        e_text3.delete(first=0,last=50)
        messagebox.showinfo('Validado','Valor Agregado')

    else:
       messagebox.showinfo('No validado','El campo no cumple los requisitos')
       #print("NO validado")        
    
#Refresh
def f_refresh():
    tree.delete(*tree.get_children())
    mibase = base.miconexion()
    micursor = mibase.cursor()
    sql = "SELECT * FROM gastos"
    micursor.execute(sql)
    resultado = micursor.fetchall()

    for x in resultado:
        tree.insert("", "end", values=x)


# Defino la ventana principal de la aplicación
root = Tk()

# Defino las variables que voy a usar
nombre = StringVar()
evento = StringVar()
gasto = IntVar()


# Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title('Gastos Mensuales')

# Creo las etiquetas y los botones
l_Nombre = ttk.Label(root, text="Nombre")
l_Evento = ttk.Label(root, text="Evento")
l_Costo = ttk.Label(root, text="Gasto")
l_Space = ttk.Label(root, text=" ")
e_text1 = ttk.Entry(root, textvariable=nombre, width=15)
e_text2 = ttk.Entry(root, textvariable=evento, width=15)
e_text3 = ttk.Entry(root, textvariable=gasto, width=15)

b_agregar = ttk.Button(root, text='Agregar', command=f_agregar)
b_refresh = ttk.Button(root, text='Mostrar', command=f_refresh)
b_salir = ttk.Button(root, text='Salir', command=root.quit)
b_creardb = ttk.Button(root, text='Crear DB', command=base.f_creardb)

#Treeview
tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=0, minwidth=0)
tree.column("col1", width=50, minwidth=50)
tree.column("col2", width=100, minwidth=100)
tree.column("col3", width=100, minwidth=100)
tree.column("col4", width=100, minwidth=100)

tree.heading("col1", text="ID")
tree.heading("col2", text="Persona")
tree.heading("col3", text="Evento")
tree.heading("col4", text="Gasto")

style = ttk.Style()
style.configure(".", font=('Tahoma', 10), foreground="royal blue")
style.configure("Treeview.Heading", foreground='maroon3')

b_agregar.grid(column=4, row=0)
b_refresh.grid(column=4, row=1)
b_salir.grid(column=4, row=8) 
b_creardb.grid(column=0, row=8)

# Posiciono los controles
l_Nombre.grid(column=0, row=0)
l_Evento.grid(column=0, row=1)
l_Costo.grid(column=0, row=2)
l_Space.grid(column=0, row=3)
e_text1.grid(column=1, row=0)
e_text2.grid(column=1, row=1)
e_text3.grid(column=1, row=2)

tree.grid(column=0, row=6, columnspan=6)

mainloop()