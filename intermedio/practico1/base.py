import mysql.connector
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
        messagebox.showinfo('No Valido','Ya existe la base de datos')

#Conexion
def miconexion():
    mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="gastos_casa")
    return mibase
