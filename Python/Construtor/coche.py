
""" 
class Coche:

    #Atributos o Propiedades (variables)
    #Caracteristica del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo= "Aventador"
    velocidad = 300
    caballaje = 500
    plaza = 2

    def __init__(self, color, marca, modelo, velocidad, caballaje, plaza):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plaza = plaza

    #metodo, sonn acciones que hace el objeto (Funciones)

    def setColor(self, color):
        self.color = color

    def getColor(self):    
        return self.color 
    # le puede dar el valor

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self, marca):
        return self.marca    

    #saca el valor de la propiedad
    def getModelo(self):
        return self.modelo   
    
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1    

    def getVelocidad(self):
        return self.velocidad
    def getInfo(self):

        info = "----- Informacion del coche -----"
        info += "\n Color: " + self.setColor()
        info += "\n Marca: " + self.setMarca()
        info += "\n Modelo: " + self.setModelo()
        info += "\n Velocidad: " + str(self.setVelocidad())

        return info
"""

class Coche:

    def __init__(self, color, marca, modelo, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def getColor(self):
        return self.color

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "----- Informacion del coche -----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info


