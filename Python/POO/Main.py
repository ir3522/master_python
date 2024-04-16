#POO

#definir una clase (molde para crear mas objeto de ese tipo)
#(coche con caracteristica  similares)

class Coche:

    #Atributos o Propiedades (variables)
    #Caracteristica del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo= "Aventador"
    velocidad = 300
    caballaje = 500
    plaza = 2

    #metodo, sonn acciones que hace el objeto (Funciones)

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
    
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1    

    def getVelocidad(self):
        return self.velocidad
    
# fin de definir de clase
# 
# crear objeto / instancia de clase
coche = Coche()

coche.setColor("Amarillo")
coche.setModelo("murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad Actual:", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad Nueva:", coche.getVelocidad())



        


