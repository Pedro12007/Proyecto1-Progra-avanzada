from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, correo, fecha_nacimiento):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    @abstractmethod
    def mostrar_info(self):
        return f"|Nombre: {self.nombre}|Correo: {self.correo}|Fecha de nacimiento: {self.fecha_nacimiento}|Rol: {self.rol}|"

class Estudiante(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, carnet, carrera):
        super().__init__(nombre, correo, fecha_nacimiento)
        self.__rol = 'estudiante'
        self.__carnet = carnet
        self.__carrera = carrera
        self.cursos=[]

    def mostrar_info(self):
        return super().mostrar_info() + f"Carnet: {self.carnet}|Carrera: {self.carrera}"

    def acceder_sistema(self):
        print('ACCESO AL SISTEMA DE ESTUDIANTE\n')
        while True:
            print("1. Inscribirse en un curso.\n"
                  "2. Consultar mis cursos.\n"
                  "3. ver mis evaluaciones.\n"
                  "4. Consultar mis calificaciones.")
            option = int(input("Ingrese una opción: "))
            match option:
                case 1:
                    print("-"*10 + "INSCRIBIRSE EN UN CURSO. " + "-"*10)
                    nombre = input("Ingrese nombre: ")
                    correo = input("Ingrese un correo: ")
                    fecha_nacimiento = int(input("Ingrese año de nacimiento: "))
                    carnet = input("Ingrese carnet: ")
                    carrera = input("Ingrese carrera:  ")


    @property
    def carnet(self):
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
        return super().mostrar_info()+f"|Codigo de empleado: {self.codigo_empleado}"

    def acceder_sistema(self):
        print('ACCESO AL SISTEMA DE ESTUDIANTE\n')
        while True:
            print("1. Consultar mis cursos asignados")
            print("2. Ver estudiantes inscritos")
            print("3. Crear evaluaciones")
            print("4. Registrar calificaciones")
            opcion= input("Ingrese una de las opciones: ")
            match opcion:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass

    @property
    def codigo_empleado(self):
        return self.__codigo_empleado

    @property
    def rol(self):
        return self.__rol