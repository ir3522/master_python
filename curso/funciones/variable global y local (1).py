# variable global
frase = " texto de variable global"

print(frase)


def holamundo():

    frase = "hola"
    print(frase)
    ## aqui se realiza una variable global
    global year 
    year ="2023"
    
    return year
print(holamundo())
# lo que se coloque aqui no sae a menos que sea una variable global