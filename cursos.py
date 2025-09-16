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

    def ver_estudiantes_inscritos(self, usuarios):
        if self.estudiantes:
            print(f"Estudiantes inscritos en el curso '{self.nombre}':")
            for i, estudiante_id in enumerate(self.estudiantes, 1):
                if estudiante_id in usuarios.usuarios:
                    estudiante = usuarios.usuarios[estudiante_id]
                    print(f"{i}. {estudiante.mostrar_info()}")
        else:
            print("No hay estudiantes inscritos en este curso.")

    def mostar_info(self):
        return f"|Id: {self.id_curso}|Nombre: {self.nombre}|Instructor: {self.instructor}|"

class Evaluacion:
    def __init__(self, id, estatus, descripcion, punteo):
        self.__id = id
        self.estatus = estatus # abierta/cerrada
        self.descripcion = descripcion
        self.punteo = punteo
        self.notas = {}

    def registrar_calificacion(self):
        pass

    def mostrar_info(self):
        return f'|Id: {self.id}|Descripción: {self.descripcion}|Estatus: {self.estatus}|Punteo: {self.punteo}|'

    @property
    def id(self):
        return self.__id