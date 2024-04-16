from tkinter import *

#definir ventana
ventana = Tk()

ventana.geometry("500x500")
ventana.title("Master en python tkinter")
ventana.resizable(0, 0)

# Ocultar otras pantallas
def ocultar():
    home_label.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()
 
 
def home():
    ocultar()
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)
 
    # Ocultar otras pantallas
    add_label.grid_remove()
 
    return True
 
def add():
    ocultar()
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
 
    return True
 
def info():
    ocultar()
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
 
    
    data_label.grid(row=1, column=0)
 
    return True
 
# Definir campos de pantalla (HOME)
home_label = Label(ventana, text="Inicio")
 
# Definir campos de pantalla (ADD)
add_label = Label(ventana, text="Añadir producto")
 
# Definir campos de pantalla (INFO)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por EdwinQr")
 
# Cargar pantalla inicio
home()