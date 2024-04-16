
"""
Proyecto python y mysql:
-Abrir Asistente:
-login 
- si elegimos un registro
- crear modifica notas
"""

from usuarios import acciones

print("""
Acciones disponible:
      - registro
      - login 

""")


hazEL = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEL.registro()

elif accion == "login":
    hazEL.login()