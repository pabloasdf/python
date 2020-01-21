from tkinter import *
from tkinter import ttk
import mysql.connector
import re
from tkinter import scrolledtext
from tkinter import messagebox


# Crear base de datos
def f_creardb():
    try:
        mibase = mysql.connector.connect(host="localhost", user="root", passwd="")
        micursor = mibase.cursor()
        micursor.execute("CREATE DATABASE gastos_casa")
        mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="gastos_casa")
        micursor = mibase.cursor()
        micursor.execute("CREATE TABLE gastos( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, evento varchar(128) COLLATE utf8_spanish2_ci NOT NULL, monto varchar(128) COLLATE utf8_spanish2_ci NOT NULL )")
        print("Base de datos con tabla creada")
    except:
        print("Ya existe la base de datos con su tabla")

#Conexion
def miconexion():
    mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="gastos_casa")
    return mibase

#Agregar
def f_agregar():
    print("Nueva alta de datos")

    cadena = nombre.get()
    patron="^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    if(re.match(patron, cadena)):
        mibase = miconexion()
        micursor = mibase.cursor()
        sql = "INSERT INTO gastos (nombre, evento, monto) VALUES (%s, %s, %s)"
        datos =(nombre.get(), evento.get(), gasto.get())
        micursor.execute(sql, datos)
        mibase.commit()
        
    else:
       print("NO validado")        
    
#Refresh
def f_refresh():
    tree.delete(*tree.get_children())
    mibase = miconexion()
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

e_text1 = ttk.Entry(root, textvariable=nombre, width=15)
e_text2 = ttk.Entry(root, textvariable=evento, width=15)
e_text3 = ttk.Entry(root, textvariable=gasto, width=15)

b_agregar = ttk.Button(root, text='Agregar', command=f_agregar)
b_refresh = ttk.Button(root, text='Refresh', command=f_refresh)
b_salir = ttk.Button(root, text='Salir', command=root.quit)
b_creardb = ttk.Button(root, text='Crear DB', command=f_creardb)

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
b_salir.grid(column=4, row=5) 
b_creardb.grid(column=0, row=5)

# Posiciono los controles
l_Nombre.grid(column=0, row=0)
l_Evento.grid(column=0, row=1)
l_Costo.grid(column=0, row=2)
e_text1.grid(column=1, row=0)
e_text2.grid(column=1, row=1)
e_text3.grid(column=1, row=2)
tree.grid(column=0, row=3, columnspan=3)

mainloop()