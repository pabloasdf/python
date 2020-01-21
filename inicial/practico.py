from tkinter import *
from tkinter import ttk
import mysql.connector
import re
from tkinter import scrolledtext
from tkinter import messagebox


# Crear base de datos

def crearbd():
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


def miconexion():
    mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="gastos_casa")
    return mibase

def alta():
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

b_agregar = ttk.Button(root, text='Agregar', command=alta)
b_refresh = ttk.Button(root, text='Refresh')#, command=fborrar)
b_salir = ttk.Button(root, text='Salir', command=root.quit)
b_creardb = ttk.Button(root, text='Crear DB', command= crearbd)

tree = ttk.Treeview(root)
tree["columns"] = ("col1")
tree.column("#0", width=0, minwidth=0, stretch=NO)
tree.column("col1", width=400, minwidth=100, stretch=NO)
tree.heading("col1", text="Tabla")
style = ttk.Style()
style.configure(".", font=('Tahoma', 10), foreground="black")
style.configure("Treeview.Heading", foreground='red')

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