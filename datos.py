from abc import ABC, abstractmethod
from cursos import Curso
class Datos(ABC):
    @abstractmethod
    def cargar_datos(self):
        pass

    @abstractmethod
    def guardar_datos(self):
        pass

class DatosUsuarios(Datos):
    def __init__(self):
        self.usuarios = {} # {id_usuario: Estudiante/Instructor}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass

class DatosCursos(Datos):
    def __init__(self):
        self.cursos = {} # {id_curso: Curso}
        self.cargar_datos()


    def cargar_datos(self):
        try:
            with open("cursos.txt","r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_curso,nombre,instructor= linea.split(":")
                        curso= Curso(id_curso,nombre,instructor)
                        self.cursos[curso.id_curso]=curso
            print("Cursos importados desde cursos.txt")
        except FileNotFoundError:
            print("No existe el archivo cursos.txt, se creará uno nuevo al guardar")
    def guardar_datos(self):
        pass


class DatosEvaluaciones(Datos):
    def __init__(self):
        self.evaluaciones = {} # {id_eval: Evaluacion}
        self.cargar_datos()

    def cargar_datos(self):
        pass

    def guardar_datos(self):
        pass