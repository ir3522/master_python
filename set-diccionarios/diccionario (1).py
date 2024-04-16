"""
un tipo de datos que amarnaceja un conjunto de datos
"""


persona = {
    "Nombre": "Isaac",
    "Apellido": "Romero",
    "Email": "ir3522@gmail.com"

}
print(type(persona))
print(persona)

print(persona["Apellido"])

# lista con diccionarios

contactos =[
    {
        'Nombre': 'isaac',
        'Email': 'ir3522@gmail.com'
    },
    {

        
        'Nombre': 'jose',
        'Email': 'ir3522@gmail.com'
    }

]
contactos[0]['Nombre'] = "pedro"
print(contactos[0]['Nombre'])  

print("\nListado de Contactos")

for contacto in contactos:
    
    print(f"Nombre de contactos: {contacto['Nombre']}")
