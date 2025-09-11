from abc import ABC, abstractmethod

class Datos(ABC):
    @abstractmethod
    def cargar_datos(self):
        pass

    @abstractmethod
    def guardar_datos(self):
        pass

    @abstractmethod
    def agregar_datos(self):
        pass

class DatosUsuarios(Datos):
    def __init__(self):
        self.usuarios = {} # {id_usuario: Estudiante/Instructor}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

    def agregar_datos(self):
        pass

class DatosCursos(Datos):
    def __init__(self):
        self.cursos = {} # {id_curso: Curso}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

    def agregar_datos(self):
        pass

class DatosEvaluaciones(Datos):
    def __init__(self):
        self.evaluaciones = {} # {id_eval: Evaluacion}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

    def agregar_datos(self):
        pass