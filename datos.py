from abc import ABC, abstractmethod
from cursos import Evaluacion
from cursos import Curso
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
        with open("cursos.txt","w",encoding="utf-8") as archivo:
            for id_curso, curso in self.cursos.items():
                archivo.write(f"\n{curso.id_curso}:{curso.nombre}:{curso.instructor}")
    def agregar_datos(self,id_curso,nombre,instructor):
        if id_curso in self.cursos:
            print("Id ya registrado")
        else:
            self.cursos[id_curso]= Curso(id_curso,nombre,instructor)
            self.guardar_datos()
            print("Curso agregado correctamente")

class DatosEvaluaciones(Datos):
    def __init__(self):
        self.evaluaciones = {} # {id_eval: Evaluacion}
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open("Evaluaciones.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_eval, estatus, descripcion, punteo = linea.split(":")
                        self.evaluaciones[id_eval]= {
                            "Estatus": estatus,
                            "Descripcion": descripcion,
                            "Punteo": punteo

                        }
            print("Evaluaciones importadas desde 'Evaluaciones,txt'")
        except FileNotFoundError:
            print("No existe el archivo 'Evaluaciones.txt', se creara uno al guardar. ")

    def guardar_datos(self):
        with open("Evaluaciones.txt", "w", encoding="utf-8")as archivo:
            for id, datos in self.evaluaciones.items():
                archivo.write(f"{id}:{datos['Estatus']}:{datos['Descripcion']}:{datos*['Punteo']}\n")

    def agregar_datos(self, id_eval, estatus, descripcion, punteo):
        if id_eval in self.evaluaciones:
            return "Id ya registrado"
        else:
            self.evaluaciones[id_eval] = Evaluacion[id_eval, estatus, descripcion, punteo]
            self.guardar_datos()