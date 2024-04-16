# variable global
nonbre = "isaac romero"

# la funcion normal
print(nonbre)
# tipo de datos que tiene la variable
print(type(nonbre))

# detectar el tipado
comprobar = isinstance(nonbre, str)
# str si es string, int si es entero
if comprobar:
    print("variable es true")
else:    
    print("no es una cadena")    

if not isinstance(nonbre, float):    
    print("la variable no es un numero con decimales")

# limpia espacio
frase = "    mi contenido"
print(frase)
#limpia  los espacio a travez de esa funcion
print(frase.strip())