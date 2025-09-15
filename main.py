from datos import DatosUsuarios, DatosCursos, DatosEvaluaciones

usuarios = DatosUsuarios()
cursos = DatosCursos()
evaluaciones = DatosEvaluaciones()

class MenuPrincipal:
    def __init__(self):
        pass

    def ejecutar_menu(self):
        while True:
            print("-" * 10 + "REGISTRO ESTUDIANTES" + "-" * 10 + "\n"
                 "1. Registrar usuario \n"
                 "2. Ingresar al sistema \n"
                 "3. Administrar cursos \n"
                 "4. Salir")
            option = input("Ingrese una opción: ")
            match option:
                case '1':
                    pass
                case '2':
                    mostrar_datos = usuarios.mostrar_datos()
                    if mostrar_datos:
                        id_usuario = input('Ingrese el id del usuario (carnet o código de empleado): ')
                        if id_usuario in usuarios.usuarios:
                            usuarios.usuarios[id_usuario].acceder_sistema()
                        else:
                            print('El id ingresado no existe.')
                case '3':
                    pass
                case '4':
                    print('Saliendo del programa...')
                    break
                case _:
                    print('Opción inválida. Intente nuevamente.\n')

menu = MenuPrincipal()
menu.ejecutar_menu()