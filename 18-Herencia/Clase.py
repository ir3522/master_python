#Herencia es la posibilidad de compartir atributos y metodos
#entre clases. y que diferentes clases herenden de otras

class Persona:
    """
    nombre
    apellido
    altura
    edad
    
    """
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.getApellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad
    def hablar(self):
        return "Estoy Hablando"
    
    def caminar(self):
        return "Estoy Caminando"
    
    def dormir(self):
        return "Estoy Durmiendo"
    
class Informatico(Persona):
    """
    lenguaje
    experiencia
    """    
    def __init__(self):
        self.lenguaje = "HTML, CCS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguaje    

    def aprender(self, lenguajes):
        self.lenguaje = lenguajes
        return self.lenguaje       

    def programar(self):
        return "Estoy Programando"
    
    def repararPC(self):
        return "estoy reparando"
    
    



