from io import open
import pathlib
import shutil

# abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/archivo.txt"
print(ruta)
archivo = open(ruta, "a+")


#escribir
archivo.write("***text desde python**\n")

# cerrar archivos
archivo.close()


# abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/archivo.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

#leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

# upper pone las cosas en mayuscula
for frase in lista:
    print("- "+frase.upper())

#copiar
"""
ruta_original = str(pathlib.Path().absolute()) + "/archivo.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/archivo_copia.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "../nueva/archivo_copia88.txt"

shutil.copyfile(ruta_original, ruta_nueva)

"""
#mover
ruta_original = str(pathlib.Path().absolute()) + "/archivo.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/archivo_nuevo.txt"

shutil.move(ruta_original, ruta_nueva)

# Eliminar
import os 
ruta_nueva = str(pathlib.Path().absolute()) + "/archivo_nuevo.txt"

os.remove(ruta_nueva)

# comprobar si un archivo existe o no
import os.path

print(os.path.abspath("../"))