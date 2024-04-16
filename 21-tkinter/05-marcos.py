from tkinter import * 

ventana = Tk()
ventana.title("marcos | master python")
ventana.geometry("700x400")

marco = Frame(ventana, width=250, height=250)
marco.config(bg="red",
             bd=12,
             relief="solid",
             )

marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primero marco")
texto.pack(side=LEFT, anchor=CENTER)
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 12),
    height=4,
    width=10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)

texto.pack(fill=Y, expand=YES)
marco = Frame(ventana, width=250, height=250)
marco.config(bg="green",
             bd=12,
             relief="solid"
             )

marco.pack(side=RIGHT, anchor=SE)


ventana.mainloop()