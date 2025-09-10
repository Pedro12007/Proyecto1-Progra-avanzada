from abc import ABC, abstractmethod

class Datos(ABC):
    @abstractmethod
    def cargar_datos(self):
        pass

    @abstractmethod
    def guardar_datos(self):
        pass

class DatosUsuarios(Datos):
    def __init__(self):
        self.usuarios = {}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

class DatosCursos(Datos):
    def __init__(self):
        self.cursos = {}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

class DatosInscripciones(Datos):
    def __init__(self):
        self.cursos = {}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

class DatosEvaluaciones(Datos):
    def __init__(self):
        self.evaluaciones = {}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass