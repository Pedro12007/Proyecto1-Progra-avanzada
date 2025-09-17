from datos import DatosUsuarios, DatosCursos, DatosEvaluaciones #USAMOS LIBRERIAS PARA IMPORTAR LOS OTROS ARCHIVOS DE DATOS
from usuarios import Estudiante, Instructor #USAMOS LIBRERIAS PARA IMPORTAR LOS OTROS ARCHIVOS DE USUARIOS
usuarios = DatosUsuarios()
cursos = DatosCursos()
evaluaciones = DatosEvaluaciones()

class MenuPrincipal: #CLASE MENU PRINCIPAL
    def __init__(self):
        pass

    def ejecutar_menu(self): # CLASE EJECUTAR MENU, el cual saldra frente al usuario
        while True:
            print("-" * 10 + "REGISTRO ESTUDIANTES" + "-" * 10 + "\n"
                 "1. Registrar usuario \n"
                 "2. Ingresar al sistema \n"
                 "3. Administrar cursos \n"
                 "4. Salir")
            option = input("Ingrese una opción: ") #OPCIONES de registro
            match option:
                case '1': #OPCION REGISTRAR USUARIO
                    print("-"*10 +"REGISTRO DE USUARIO"+ "-"*10)
                    print("1. Estudiante\n"
                          "2. Instructor")
                    option = input("Ingrese una opcion: ")
                    if option == '1': #CUANDO EL USUARIO ELIJE ESTUDIANTE
                        print("-"*10+"REGISTRAR ESTUDIANTES" +"-"*10)
                        nombre = input("Ingrese nombre: ")
                        correo = input("Ingrese correo: ")
                        nacimiento = int(input("Ingrese el año de nacimiento: "))
                        carnet = input("Ingrese carnet: ")
                        carrera = input("Ingrese carrera: ")
                        nuevo_estudiante = Estudiante(nombre, correo, nacimiento, carnet, carrera) #SE GUARDA EN LA CLASE ESTUDIANTE
                        usuarios.agregar_datos(nuevo_estudiante) #SE AGREGAN LOS DATOS
                    elif option == '2': #CUANDO EL USUARIO ELIJE INSTRUCTOR
                        print("-"*10+"REGISTRAR INSTRUCTORES"+"-"*10)
                        nombre = input("Ingrese nombre: ")
                        correo = input("Ingrese correo: ")
                        nacimiento = int(input("Ingrese el año de nacimiento: "))
                        code_empleado = input("Ingrese el codigo de empleado del instructor: ")
                        nuevo_instructor = Instructor(nombre, correo, nacimiento, code_empleado) #SE GUARDA EN LA CLASE INSTRUCTOR
                        usuarios.agregar_datos(nuevo_instructor) #SE AGREGAN LOS DATOS AL DICCIONARIO
                case '2': #OPCION INGRESAR AL SISTEMA
                    mostrar_datos = usuarios.mostrar_datos()
                    if mostrar_datos:
                        id_usuario = input('Ingrese el id del usuario (carnet o código de empleado): ')
                        if id_usuario in usuarios.usuarios:
                            usuarios.usuarios[id_usuario].acceder_sistema(cursos, evaluaciones, usuarios) #MUESTRA LOS DATOS DESDE LA FUNCION acceder_sistema
                        else:
                            print('El id ingresado no existe.')
                case '3': #OPCION ADMINISTRAR CURSOS
                    while True:
                        print("-"*10+"ADMINISTRAR CURSOS"+ "-"*10)
                        print("1. Crear curso")
                        print("2. Asignar curso a instructor")
                        print("3. Consultar cursos")
                        print("4. Generar reportes")
                        print("5. Volver a menu principal")
                        opcion= input("Ingrese una de las opciones: ")
                        match opcion:
                            case "1": #OPCION CREAR CURSO
                                id_curso= input("Ingrese código del curso: ")
                                nombre= input("Ingrese el nombre del curso: ")
                                instructor= input("Ingrese el codigo del instructor: ")
                                cursos.agregar_datos(id_curso,nombre,instructor) #SE CREA EL CURSO Y SE GUARDA
                            case "2": #OPCION ASIGNAR CURSO A INSTRUCTOR
                                id_curso= input("Ingrese el id del curso: ")
                                codigo_instructor= input("Ingrese el codigo del instructor: ")
                                if id_curso in cursos.cursos and codigo_instructor in usuarios.usuarios:
                                    curso= cursos.cursos[id_curso]
                                    instructor= usuarios.usuarios[codigo_instructor]
                                    curso.instructor = codigo_instructor
                                    instructor.cursos_asignados.append(id_curso)
                                    cursos.guardar_datos()
                                    usuarios.guardar_datos() #SE LE ASIGNA EL CURSO, SE GUARDA
                                    print(f"Curso {id_curso} asignado a instructor {codigo_instructor}") #MENSAJE HACIA EL USUARIO
                                else:
                                    print("Curso o instructor no encontrado")
                            case "3": #OPCION CONSULTAR CURSO
                                    cursos.mostrar_datos() #MUESTRA SI HAY CURSOS ASIGNADOS
                            case "4": #OPCION GENERAR REPORTE
                                print("-" + "Reporte de estudiantes con promedio bajo"+"-"*10 + "\n")
                                for curso in cursos.cursos.values():
                                    notas_por_estudiante={} #{carnet: [notas]}
                                    for id_evaluacion in curso.evaluaciones:
                                        if id_evaluacion in evaluaciones.evaluaciones:
                                            evaluacion= evaluaciones.evaluaciones[id_evaluacion]
                                            for estudiante, nota in evaluacion.notas.items():
                                                if estudiante not in notas_por_estudiante:
                                                    notas_por_estudiante[estudiante]= []
                                                notas_por_estudiante[estudiante].append(nota)
                                    for estudiante, notas in notas_por_estudiante.items():
                                        if notas:
                                            promedio= sum(notas)/len(notas)
                                            if promedio < 60:
                                                if estudiante in usuarios.usuarios:
                                                    nombre_estudiante= usuarios.usuarios[estudiante].nombre
                                                print(f"Curso: {curso.nombre}|Estudiante: {nombre_estudiante} ({estudiante}|Promedio: {promedio:.2f}|")

                            case "5": #VOLVER AL MENU PRINCIPAL
                                break
                case '4': #SALIR
                    print('Saliendo del programa...')
                    break
                case _:
                    print('Opción inválida. Intente nuevamente.\n')

menu = MenuPrincipal()
menu.ejecutar_menu()