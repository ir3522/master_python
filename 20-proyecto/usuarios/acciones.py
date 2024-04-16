import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):

        print("\n Ok !! vamos a registrarte en el sistema")

        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce una contrasena: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("\nNo te haz registrado correctamente")

    def login(self):

        print("vale identificate en el sistema")

        try:
        
            email = input("Introduce tu email: ")
            password = input("Introduce una contrasena: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            #[] es el indice en la base de datos
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema {login[5]}")
                self.proximasAcciones(login)


        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponible:
        - Crear nota(crear)
        - Mostrar tus notas(mostrar)
        - Eliminar nota (eliminar)
        - Salir(salir)   
                          
        """)
        
        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar") 
            self.proximasAcciones(usuario)            

        elif accion == "salir":
            print(f"ok {usuario[1]}, hasta pronto ")
            exit()

        return None        
        

    



