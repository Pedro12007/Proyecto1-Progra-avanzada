class Curso:
    def __init__(self, id, nombre, instructor):
        self.__id = id
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []

    @property
    def id_curso(self):
        return self.__id

    @id_curso.setter
    def id_curso(self,id):
        self.__id = id

    def inscribir_estudiante(self, estudiante_id):
        if estudiante_id not in self.estudiantes:
            self.estudiantes.append(estudiante_id)
        else:
            print('Estudiante ya registrado.')

    def agregar_evaluacion(self, evaluacion_id):
        if evaluacion_id not in self.evaluaciones:
            self.estudiantes.append(evaluacion_id)
        else:
            print('Estudiante ya registrado.')

class Evaluacion:
    def __init__(self, id, estatus, descripcion, punteo):
        self.__id = id
        self.estatus = estatus
        self.descripcion = descripcion
        self.punteo = punteo
        self.notas = {}

    def registrar_calificacion(self):
        pass
    @property
    def id(self):
        return self.__id