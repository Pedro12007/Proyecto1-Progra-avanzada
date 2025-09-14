class MenuPrincipal:
    def __init__(self):
        pass

    def ejecutar_menu(self):
        while True:
            print("-" * 10 + "REGISTRO ESTUDIANTES" + "-" * 10 + "\n"
                 "1. Registrar usuario \n"
                 "2. Ingresar Estudiante \n"
                 "3. Ingresar Instructor \n"
                 "4. Administrar cursos \n"
                 "5. Salir")
            option = int(input("Ingrese una opcion: "))
            match option:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print('Saliendo del programa...')
                    break

menu = MenuPrincipal()
menu.ejecutar_menu()