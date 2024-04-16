cantantes = ['2pac', 'Drake', 'Julio Iglesia']
numeros = [1, 2, 5, 8, 3, 4]

#ordenar

print(numeros)
numeros.sort()
print(numeros)

#añadir elementos

cantantes.append("natos")
cantantes.insert(1,"david divar")
print(cantantes)

# eliminar elementor

cantantes.pop(1)
cantantes.remove('Drake')
print(cantantes)

# dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

# buscar 

print('Drake' in cantantes)

# contar

print(len(cantantes))

# cuanta veces aparece
print(numeros.count(8))

# conseguir indice

print(cantantes.index("natos"))

# unir lista

cantantes.extend(numeros)
print(cantantes)
