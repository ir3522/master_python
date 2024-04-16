from tkinter import *

ventana = Tk()
ventana.geometry("500x500") 

texto = Label(ventana, text ="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="black",
           #margenes
            padx=20,
            pady=20,
            font=("Arial", 30)
            
)

texto.pack()

def pruebas(nombre, apellido, pais):
    return f"Hola {nombre} {apellido} veo que eres de  {pais} "

texto = Label(ventana, text =pruebas(nombre="Isaac",apellido="Romero", pais="Venezuela"))
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
 
)

texto.pack(anchor=W)

# pack enpaqueta para que aparezca

ventana.mainloop()

