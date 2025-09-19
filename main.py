from datos import DatosUsuarios, DatosCursos, DatosEvaluaciones #USAMOS LIBRERIAS PARA IMPORTAR LOS OTROS ARCHIVOS DE DATOS
from usuarios import Estudiante, Instructor #USAMOS LIBRERIAS PARA IMPORTAR LOS OTROS ARCHIVOS DE USUARIOS
import datetime

usuarios = DatosUsuarios()
cursos = DatosCursos()
evaluaciones = DatosEvaluaciones()

def validacion_nacimiento():
    while True:
        try:
            nacimiento = int(input("Ingrese el año de nacimiento: "))
            if datetime.datetime.now().year >= nacimiento > 1900:
                return nacimiento
            else:
                print('Por favor, ingrese un año válido.')
                continue
        except ValueError:
            print("Por favor, ingrese un año válido (número entero).")

class MenuPrincipal: #CLASE MENU PRINCIPAL
    def __init__(self):
        pass

    def ejecutar_menu(self): # CLASE EJECUTAR MENU, el cual saldrá frente al usuario
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
                    option = input("Ingrese una opción: ")
                    if option == '1': #CUANDO EL USUARIO ELIGE ESTUDIANTE
                        print("-"*10+"REGISTRAR ESTUDIANTES" +"-"*10)
                        nombre = input("Ingrese nombre: ")
                        correo = input("Ingrese correo: ")
                        nacimiento = validacion_nacimiento()
                        carnet = input("Ingrese carnet: ")
                        carrera = input("Ingrese carrera: ")
                        if nombre and correo and carnet and carrera:
                            nuevo_estudiante = Estudiante(nombre, correo, nacimiento, carnet, carrera) #SE GUARDA EN LA CLASE ESTUDIANTE
                            usuarios.agregar_datos(nuevo_estudiante) #SE AGREGAN LOS DATOS
                        else:
                            print("Los campos no pueden quedar vacíos")
                    elif option == '2': #CUANDO EL USUARIO ELIGE INSTRUCTOR
                        print("-"*10+"REGISTRAR INSTRUCTORES"+"-"*10)
                        nombre = input("Ingrese nombre: ")
                        correo = input("Ingrese correo: ")
                        nacimiento = validacion_nacimiento()
                        code_empleado = input("Ingrese el código de empleado del instructor: ")
                        if nombre and correo and code_empleado:
                            nuevo_instructor = Instructor(nombre, correo, nacimiento, code_empleado) #SE GUARDA EN LA CLASE INSTRUCTOR
                            usuarios.agregar_datos(nuevo_instructor) #SE AGREGAN LOS DATOS AL DICCIONARIO
                        else:
                            print("Los campos no pueden quedar vacíos.")
                    else:
                        print("Ingrese una opción correcta")
                case '2': #OPCION INGRESAR AL SISTEMA
                    mostrar_datos = usuarios.mostrar_datos()
                    if mostrar_datos:
                        id_usuario = input('Ingrese el id del usuario (carnet o código de empleado): ')
                        if id_usuario in usuarios.usuarios:
                            usuarios.usuarios[id_usuario].acceder_sistema(cursos, evaluaciones, usuarios) #MUESTRA LOS DATOS DESDE LA FUNCIÓN acceder_sistema
                        else:
                            print('El id ingresado no existe.')
                case '3': #OPCION ADMINISTRAR CURSOS
                    while True:
                        print("-"*10+"ADMINISTRAR CURSOS"+ "-"*10)
                        print("1. Crear curso")
                        print("2. Consultar cursos")
                        print("3. Generar reportes")
                        print("4. Volver a menu principal")
                        opcion= input("Ingrese una de las opciones: ")
                        match opcion:
                            case "1": #OPCION CREAR CURSO
                                print("\nInstructores disponibles:")
                                for id_usuario, usuario in usuarios.usuarios.items():
                                    if isinstance(usuario,Instructor):  # O si usas rol: if usuario.rol == "instructor":
                                        print(f"  ID: {id_usuario} | Nombre: {usuario.nombre}")
                                id_curso= input("Ingrese código del curso: ")
                                nombre= input("Ingrese el nombre del curso: ")
                                instructor= input("Ingrese el código del instructor: ")
                                if instructor in usuarios.usuarios and isinstance(usuarios.usuarios[instructor], Instructor):
                                    cursos.agregar_datos(id_curso,nombre,instructor) #SE CREA EL CURSO Y SE GUARDA
                                else:
                                    print('El usuario no existe o no es instructor.')
                            case "2": #OPCION CONSULTAR CURSO
                                    cursos.mostrar_datos() #MUESTRA SI HAY CURSOS ASIGNADOS
                            case "3": #OPCION GENERAR REPORTE
                                encontrados = False
                                print("-"*10 + "Reporte de estudiantes con promedio bajo"+"-"*10 + "\n")
                                for curso in cursos.cursos.values():
                                    notas_por_estudiante={} #{carnet: [notas]}
                                    for id_evaluacion in curso.evaluaciones:
                                        if id_evaluacion in evaluaciones.evaluaciones:
                                            evaluacion= evaluaciones.evaluaciones[id_evaluacion]
                                            for estudiante, nota in evaluacion.notas.items():
                                                if estudiante not in notas_por_estudiante:
                                                    notas_por_estudiante[estudiante]= []
                                                porcentaje_nota = nota/evaluacion.punteo*100
                                                notas_por_estudiante[estudiante].append(porcentaje_nota)
                                    for estudiante, notas in notas_por_estudiante.items():
                                        if notas:
                                            promedio= sum(notas)/len(notas)
                                            if promedio < 60:
                                                encontrados = True
                                                if estudiante in usuarios.usuarios:
                                                    nombre_estudiante= usuarios.usuarios[estudiante].nombre
                                                    print(f"Curso: {curso.nombre}|Estudiante: {nombre_estudiante} ({estudiante}|Promedio: {promedio:.2f}%|")

                                if not encontrados:
                                    print("-"*10 + 'No hay estudiantes con promedio bajo.'+ "-"*10)

                            case "4": #VOLVER AL MENU PRINCIPAL
                                break
                            case _:
                                print("Ingrese una opción válida.")
                case '4': #SALIR
                    print('Saliendo del programa...')
                    break
                case _:
                    print('Opción inválida. Intente nuevamente.\n')

menu = MenuPrincipal()
menu.ejecutar_menu()