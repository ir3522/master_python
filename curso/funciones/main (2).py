# ejemplo 2 parametro


nombre ="isaac romero"

def mostrarnombre(nombre):
    print(f" Mi nombre es: {nombre}")

nombre = input("Introduce tu nombre: ")
mostrarnombre(nombre)

# ejemplo 4 

 #aqui es una funcion normal
def getEmpleado(nombre, dni):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DIN: {dni}")

getEmpleado("Isaac", "123")    



#fin de la funcion normal 

# 
# def getEmpleado(nombre, dni = false): el false o none es el optional
# Ejemplo 5 delvolver datos

def getEmpleado(nombre, dni):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DIN: {dni}")

getEmpleado("Isaac", "123")    

#ejemplo 5 return

def saludame(nombre):
    saludo =f"hola, saludos {nombre}"

    return saludo

# llamado a  funtion saludame("jose")
print(saludame("jose"))
# el nombre lo va a tomar del input que esta arribaisaac
############################# fin de ejemplo
## ejemplo 6




def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multi: " + str(multi)
    cadena += "\n"
    cadena += "Division: " + str(division)
    cadena += "\n"

    return cadena

print(calculadora(5,5))
