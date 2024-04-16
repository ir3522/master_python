from tkinter import *

ventana = Tk()
#ventana.geometry("500x500") 

texto = Label(ventana, text ="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="black",
           #margenes
            padx=50,
            pady=20,
            font=("Consolas", 30),
            
)

texto.pack(side=TOP)



texto = Label(ventana, text="Basico1" )
texto.config(
    height=3,
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
 
)

texto.pack(side=LEFT)

# ------------------------------

texto = Label(ventana, text="Basico2" )
texto.config(
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
 
)

texto.pack(side=TOP)


texto = Label(ventana, text="Basico3" )
texto.config(
    height=3,
    bg="blue",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
 
)

texto.pack(side=RIGHT)

# pack enpaqueta para que aparezca

ventana.mainloop()

