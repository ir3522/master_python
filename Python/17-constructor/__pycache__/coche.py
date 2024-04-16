class Coche:

    

    #Atributos o Propiedades (variables)
    #Caracteristica del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo= "Aventador"
    velocidad = 300
    caballaje = 500
    plaza = 2

    soy_publico = "Hola, soy un atributo publico "
    __soyprivado__ = "soy privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plaza):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plaza = plaza
        

    #metodo, sonn acciones que hace el objeto (Funciones)
def getPrivado(sefl):
    return sefl.__soyprivado

    def setColor(self, color):
        self.color = color

    def getColor(self):    
        return self.color 
    # le puede dar el valor
    def setModelo(self, modelo):
        self.modelo = modelo

    #saca el valor de la propiedad
    def getModelo(self):
        return self.modelo   
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self, marca):
        return marca  
    
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1    

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(seft):

        info = " ----  informacion del coche ---- "
        info += "\n Color: " + seft.getColor()
        info += "\n Marca: " + seft.getMarca()
       
        info += "\n Velocidad: " + str(seft.getVelocidad())

        return info
