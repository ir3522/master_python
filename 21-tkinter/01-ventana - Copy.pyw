

from tkinter import *
import os.path

class Programa:

        def __init__(self):
              self.title = "master en python"
              self.icon = './imagenes/ventana.ico'
              self.icon_alt = './21-tkinter/imagenes/ventana.ico'
              self.size = "770x470"
              self.resizable = False
        
        def cargar(self):   
            #crea la ventana 
            ventana = Tk()
            self.ventana = ventana

            #titulo de la ventana
            ventana.title(self.title)

            #comprobar si hay un archivo
            ruta_icono = os.path.abspath(self.icon) 

            if not os.path.isfile(ruta_icono):
                ruta_icono = os.path.abspath(self.icon_alt) 
                print("no existe")
            # icono de la ventana
            ventana.iconbitmap(ruta_icono)

            #mostrar texto en la ventana
            texto = Label(ventana, text=ruta_icono)
            texto.pack()



            # cambio de tamano
            ventana.geometry(self.size)

            #bloqueo del tamano de la ventana
            if self.resizable: 
                ventana.resizable(1,1)
            else:    
                ventana.resizable(0,0)
            
            
    
        def addTexto(self):        
            texto = Label(self.ventana, text="Hola desde un metodo")    
            texto.pack()
# arrancar y mostrar la ventana        
        def mostrar(self):  
            self.ventana.mainloop() 
             
            
# instaciar mi programa            

programa = Programa()   
programa.cargar() 
programa.addTexto()
programa.mostrar()
     
               

