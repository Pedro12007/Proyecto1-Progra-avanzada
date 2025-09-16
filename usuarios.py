from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, correo, fecha_nacimiento):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    @abstractmethod
    def mostrar_info(self):
        return f"|Nombre: {self.nombre}|Correo: {self.correo}|Año de nacimiento: {self.fecha_nacimiento}|"

class Estudiante(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, carnet, carrera):
        super().__init__(nombre, correo, fecha_nacimiento)
        self.__rol = 'estudiante'
        self.__carnet = carnet
        self.__carrera = carrera
        self.cursos=[]

    def mostrar_info(self):
        return 'ESTUDIANTE: ' + super().mostrar_info() + f"Carnet: {self.__carnet}|Carrera: {self.carrera}|"

    def acceder_sistema(self, cursos, evaluaciones):
        print('ACCESO AL SISTEMA DE ESTUDIANTE\n')
        while True:
            print("1. Inscribirse en un curso.\n"
                  "2. Consultar mis cursos.\n"
                  "3. Ver mis evaluaciones.\n"
                  "4. Consultar mis calificaciones.\n"
                  "5.Salir")
            option = input("Ingrese una opción: ")
            match option:
                case '1':
                    cursos.mostrar_datos()
                    curso_id = input('Ingrese el id del curso al que desea inscribirse: ')
                    if curso_id in cursos.cursos and curso_id not in self.cursos:
                        self.cursos.append(curso_id)
                        cursos.cursos[curso_id].inscribir_estudiante(self.id)
                        cursos.guardar_datos()
                        print(f'Te has inscrito al curso con id: {curso_id}')
                    else:
                        print('Curso inexistente o ya inscrito previamente.')

                case '2':
                    pass

                case '3':
                    pass

                case '4':
                    pass

                case '5':
                    break


    @property
    def id(self):
        return self.__carnet

    @property
    def carrera(self):
        return self.__carrera

    @property
    def rol(self):
        return self.__rol

class Instructor(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, codigo_empleado):
        super().__init__(nombre, correo, fecha_nacimiento)
        self.__rol = 'instructor'
        self.__codigo_empleado = codigo_empleado
        self.cursos_asignados = []

    def mostrar_info(self):
        return 'INSTRUCTOR: ' +  super().mostrar_info()+f"|Codigo de empleado: {self.__codigo_empleado}|"

    def acceder_sistema(self, cursos, evaluaciones):
        print('ACCESO AL SISTEMA DE INSTRUCTOR\n')
        while True:
            print("1. Consultar mis cursos asignados")
            print("2. Ver estudiantes inscritos")
            print("3. Crear evaluaciones")
            print("4. Registrar calificaciones")
            print('5. Salir')
            opcion= input("Ingrese una de las opciones: ")
            match opcion:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case '4':
                    pass

                case '5':
                    pass


    @property
    def id(self):
        return self.__codigo_empleado

    @property
    def rol(self):
        return self.__rol