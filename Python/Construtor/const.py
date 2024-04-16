from coche import Coche

carro = Coche("Amarillo", "Reunat", "Clio", 150)
carro2 = Coche("Rojo", "Mercede", "S10", 150)

print(carro.getInfo())
print(carro2.getInfo())

if type(carro2) == Coche:
    print("es un objeto correcto")
else:
    print("no es un objeto correcto")    

# visibilidad
#print(carro.soy_publico) 
print(carro.getPrivado())
