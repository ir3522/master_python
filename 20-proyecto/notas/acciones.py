import notas.nota as modelo



class Acciones:

    def crear(self, usuario):
        print(f"\nok {usuario[1]} vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")


        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0]  >= 1:
            print(f"\n perfecto has guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota {usuario[1]}")    

    def mostrar(self, usuario):  
        print(f"Vale {usuario[1]} aqui tienes tus notas: ")     

        nota = modelo.nota(usuario[0]) 
        notas = nota.listar()

        print(notas)



