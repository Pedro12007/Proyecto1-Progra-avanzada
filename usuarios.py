from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, nombre, correo, fecha_nacimiento, rol):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.rol = rol

    @abstractmethod
    def mostrar_info(self):
        pass

class Estudiante(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, rol, carnet, carrera):
        super().__init__(nombre, correo, fecha_nacimiento, rol)
        self.__carnet = carnet
        self.__carrera = carrera

    def mostrar_info(self):
        pass

    def acceder_sistema(self):
        while True:
            print("1. Inscribirse en un curso.\n"
                  "2. Consultar mis cursos.\n"
                  "3. ver mis evaluaciones.\n"
                  "4. Consultar mis calificaciones.")
            option = int(input("Ingrese una opcion: "))
            match option:
                case 1:
                    print("-"*10 + "INCRIBIRSE EN UN CURSO. " + "-"*10)
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

class Instructor(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, rol, codigo_empleado):
        super().__init__(nombre, correo, fecha_nacimiento, rol)
        self.__codigo_empleado = codigo_empleado

    def mostrar_info(self):
        pass

    def acceder_sistema(self):
        pass

    @property
    def codigo_empleado(self):
        return self.__codigo_empleado