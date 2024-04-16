"""
Lista (array)
"""

"""

Pelicula = "Batman"

Peliculas = ["batman", "spideman", "el señor de los anillos"]
cantantes = list(('spa', 'drake', 'jenifer lopez'))
years = list(range(2020, 2050))

Peliculas[1] = "gran torino"
cantantes.append("kase O")

print(Peliculas[1])
print(cantantes[0:2])
print(years)
print(cantantes)
# añadir elementor a la lista


nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
            Peliculas.append(nueva_pelicula)
print("\n+++++++++++++++++++++++ ñista de peliculas +++++++++++++++++++")

for Pelicula in Peliculas:
    print(f"{Peliculas.index(Pelicula)+1}. {Pelicula}")


"""    

# lista multidimencional



print("\n+++++++++++++++++++ listado de conctatos")    
contactos =[
      
    [
          'Antonio',
          'antonio@.com'
     ],

     [
          'luis',
          'luis@.com'

     ]

]

#print(contactos[1][1])

for contacto in contactos:
         
    for elemento in contacto:
            if contacto.index(elemento) == 0:
                print("Nombre: " + elemento)
            else:
                print("Email: " + elemento)   
            print("\n")
           
