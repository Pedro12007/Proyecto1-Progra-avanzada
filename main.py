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
                    while True:
                        print("ADMINISTRAR CURSOS")
                        print("1. Crear curso")
                        print("2. Asignar curso a instructor")
                        print("3. Consultar cursos")
                        print("4. Generar reportes")
                        opcion= input("Ingrese una de las opciones: ")
                        match opcion:
                            case "1":
                                id= input("Ingrese código del curso: ")
                                nombre= input("Ingrese el nombre del curso: ")
                                instructor= input("Ingrese el codigo del instructor: ")
                                cursos.agregar_datos(id,nombre,instructor)
                case '4':
                    print('Saliendo del programa...')
                    break
                case _:
                    print('Opción inválida. Intente nuevamente.\n')

menu = MenuPrincipal()
menu.ejecutar_menu()