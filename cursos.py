class Curso:
    def __init__(self, id, nombre, instructor):
        self.__id = id
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []


    def inscribir_estudiante(self):
        pass
    @property
    def id_curso(self):
        return self.__id
    @id_curso.setter
    def id_curso(self,id):
        self.__id= id

class Evaluacion:
    def __init__(self, id, estatus, descripcion, punteo):
        self.__id = id
        self.estatus = estatus
        self.descripcion = descripcion
        self.punteo = punteo
    def registrar_calificacion(self):
        pass
    @property
    def id(self):
        return self.__id