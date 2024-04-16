import Clase

persona = Clase.Persona()
persona.setNombre("Isaac")
persona.setApellidos("Romero")
persona.setAltura("170cm")
persona.setEdad("40")

print(f"la persona es: {persona.getNombre()}")
print(persona.hablar())

informatico = Clase.Informatico()
informatico.setNombre("Carlos")

print(f"el informaticoes: {informatico.getNombre()}")