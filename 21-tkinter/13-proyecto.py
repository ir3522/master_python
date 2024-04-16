from tkinter import *

#definir ventana
ventana = Tk()

#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Master en python tkinter")
ventana.resizable(0, 0)


# ---------------------------
def ocultar():
    home_label.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()


# Pantallas
def home():
    ocultar()
    # montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=20
    )
    # para poder mostrar en la pantalla
    home_label.grid(row=0, column=0)
    
    products_box.grid(row=1)
    
    #ocultar pantalla

    #listar productos
    for product in products:
        #3 porque son tres campoos
        if len(products) == 3:
            products.append("anadido")
            Label(products_box, text=products[0]).grid
            Label(products_box, text=products[1]).grid
            Label(products_box, text=products[2]).grid
            Label(products_box, text="----------------------").grid
    return True

def add():
    # "encabezado"
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=100,
        pady=20
        
    )
    # para poder mostrar en la pantalla
    add_label.grid(row=0, column=0, columnspan=10)
    
    #campo del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    add_name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    add_price_entry.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    
    # para el boton
    add_separator.grid(row=4)
    boton.grid(row=5, column=0, sticky=E)
    boton.config(
        pady=5,
        padx=15,
        bg="black",
        fg="white"
        
    )
    
    home_label.grid.remove()
    info_label.grid.remove()
    data_label.grid.remove()
    
    return True

def info():
    
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
        
    )
    
    
    # para poder mostrar en la pantalla
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    
    # campo de formulario
    
    
    add_label.grid.remove()
    home_label.grid.remove()
    add_frame.grid_remove()
    
    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    home()
    print(products)

# Variable importante     
products = []
name_data = StringVar()  
price_data = StringVar()

# Definir campos de pantalla (HOME)
home_label = Label(ventana, text="Inicio")

# Definir campos de pantalla (ADD)

add_label = Label(ventana, text="Añadir producto")
# Campo del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data) 

add_description_label = Label(add_frame, text="Descripcion: ")
add_description_entry = Text(add_frame)
 
add_separator = Label(add_frame)
 
boton = Button(ventana, text="Guardar",command=add_product)
# Definir campos de pantalla (INFO)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Isaac")
 
# Cargar pantalla inicio

    
# definir campo de pantalla
home_label = Label(ventana, text="Inicio")
products_box = Frame(ventana, width=250)
add_label = Label(ventana, text="Anadir")
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado  por Isaac")

#cargar la pantalla inicio
home()  

#menu superior

menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Anadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)


# Cargar Menu
ventana.config(menu=menu_superior)




#cargar ventana
ventana.mainloop()