from tkinter import *


ventana = Tk()
ventana.geometry("700x500")
ventana.title(" formulario en tkinter")

#texto encabezado
encabezado = Label(ventana, text="Formulario con tkinter  isaac romero")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Arial", 18),
    padx=10,
    pady=10
)
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)
# label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

#campo de texto

#campo_texto.pack(side=LEFT, anchor=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1,  sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#otro campo 

#---------------------------------------------------------Apellido

# label para el campo
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0,  padx=5, pady=5)

#campo de texto

#campo_texto.pack(side=LEFT, anchor=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, columnspan=6, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="disabled")

#otro campo 

# label para el descripcion
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0,  padx=5, pady=5, sticky=N)

#campo_texto.pack
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1 )
campo_grande.config(
    width=30, 
    height=5,
    font=("Arial", 12), 
    padx=15,
    pady=15,
)

#boton
Label(ventana).grid(row=4, column=1)
boton = Button(ventana, text="Enviar")
boton.grid(row=4, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="green", fg="white")

ventana.mainloop()