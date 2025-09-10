from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, correo, fecha_nacimiento, rol):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.rol = rol

    @abstractmethod
    def mostrar_info(self):
        return f"|Nombre: {self.nombre}|Correo: {self.correo}|Fecha de nacimiento: {self.fecha_nacimiento}|Rol: {self.rol}"

class Estudiante(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, rol, carnet, carrera):
        super().__init__(nombre, correo, fecha_nacimiento, rol)
        self.__carnet = carnet
        self.__carrera = carrera

    def mostrar_info(self):
        pass

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
        return super().mostrar_info()+f"|Codigo de empleado: {self.codigo_empleado}"
    @property
    def codigo_empleado(self):
        return self.__codigo_empleado