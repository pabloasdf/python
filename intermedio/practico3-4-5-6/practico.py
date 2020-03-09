import tkinter as tk
from tkinter import ttk
import mysql.connector
import re
from modulo_validacion import val
from modulo_base_datos import base
from tkinter import scrolledtext
from tkinter import messagebox

class Aplicacion:
    def __init__ (self, ventana):
        #WINDOW
        self.window = ventana
        self.window.title("Gastos Mensuales")
        #self.window.geometry("600x600")
        self.window.resizable(width=False, height=False)
        #self.window.configure(background="royal blue")

        #LABELFRAME 
        self.recuadro = tk.LabelFrame(self.window, text="Ingresar Datos",fg = "royal blue")
        self.recuadro.grid(columnspan=1, pady=10, padx=10)
        #self.recuadro.configure(bg="blue")

        #LABELS
        tk.Label(self.recuadro, text="").grid(row=0, column=0)
        tk.Label(self.recuadro, text="").grid(row=0, column=2)

        tk.Label(self.recuadro, text="  Nombre ").grid(row=1, column=0)
        self.Nombre = tk.Entry(self.recuadro)
        self.Nombre.grid(row=1, column=1)
        tk.Label(self.recuadro, text="").grid(row=2, column=0)

        tk.Label(self.recuadro, text="  Evento ").grid(row=3, column=0)
        self.Evento = tk.Entry(self.recuadro)
        self.Evento.grid(row=3, column=1)
        tk.Label(self.recuadro, text="").grid(row=4, column=0)

        tk.Label(self.recuadro, text="  Gasto ").grid(row=5, column=0)
        self.Gasto = tk.Entry(self.recuadro)
        self.Gasto.grid(row=5, column=1)

        tk.Label(self.recuadro, text="  ").grid(row=8, column=0)
        tk.Label(self.recuadro, text="  ").grid(row=8, column=2)
        tk.Label(self.window, text="  ").grid(row=11, column=2)
        tk.Label(self.window, text="  ").grid(row=13, column=2)
 
        #BOTONES

        tk.Button(self.window, text="Agregar").place(x=250, y=17, width=80, height=30)
        tk.Button(self.window, text="Mostrar").place(x=250, y=117, width=80, height=30)
        tk.Button(self.window, text="Configuracion").place(x=15, y=418, width=90, height=30)
        tk.Button(self.window, text="Crear DB").place(x=145, y=418, width=80, height=30)
        tk.Button(self.window, text="Salir").place(x=260, y=418, width=80, height=30)

        #Treeview
        self.tree = ttk.Treeview(columns=("col1", "col2", "col3", "col4"))
        self.tree.grid(column=0, row=10, columnspan=6)
        self.tree.heading("col1", text="ID")
        self.tree.heading("col2", text="Persona")
        self.tree.heading("col3", text="Evento")
        self.tree.heading("col4", text="Gasto")
        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("col1", width=50, minwidth=50)
        self.tree.column("col2", width=100, minwidth=100)
        self.tree.column("col3", width=100, minwidth=100)
        self.tree.column("col4", width=100, minwidth=100)
        
        style = ttk.Style()
        style.configure(".", font=('Tahoma', 10), foreground="maroon3")


if __name__ == "__main__": 
    ventana = tk.Tk()
    App = Aplicacion(ventana)
    ventana.mainloop()