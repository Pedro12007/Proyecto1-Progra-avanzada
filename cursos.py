class Curso:
    def __init__(self, id, nombre, instructor):
        self.__id = id
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = [] #LISTA DE ESTUDIANTES
        self.evaluaciones = [] #LISTA DE EVALUACIONES

    @property #METODO GET
    def id_curso(self):
        return self.__id

    def inscribir_estudiante(self, estudiante_id): #FUNCION DE INSCRIBIR ESTUDIANTE
        if estudiante_id not in self.estudiantes:
            self.estudiantes.append(estudiante_id)
        else:
            print("-"*10+'Estudiante ya registrado.'+"-"*10)

    def agregar_evaluacion(self, evaluacion_id): #FUNCION AGREGAR EVALUACIÓN
        if evaluacion_id not in self.evaluaciones:
            self.evaluaciones.append(evaluacion_id)
        else:
            print("-"*10+'Evaluación ya registrada.'+"-"*10)

    def ver_estudiantes_inscritos(self, usuarios): #FUNCION VER ESTUDIANTES INSCRITOS
        if self.estudiantes:
            print("-"*10+ f'Estudiantes inscritos en el curso {self.nombre}' +"-"*10 )
            for i, estudiante_id in enumerate(self.estudiantes, 1):
                if estudiante_id in usuarios.usuarios:
                    estudiante = usuarios.usuarios[estudiante_id]
                    print(f"{i}. {estudiante.mostrar_info()}") #IMPRIME LOS ESTUDIANTES INSCRITOS
        else:
            print("No hay estudiantes inscritos en este curso.")

    def ver_evaluaciones(self, evaluaciones):
        if self.evaluaciones:
            print(f"Evaluaciones del curso '{self.nombre}':") #MUESTRA EVALUCIONES SI ESTÁN ASIGNADAS
            for i, evaluacion_id in enumerate(self.evaluaciones, 1):
                if evaluacion_id in evaluaciones.evaluaciones:
                    evaluacion = evaluaciones.evaluaciones[evaluacion_id]
                    print(f"{i}. {evaluacion.mostrar_info()}")
        else:
            print("No hay evaluaciones asignadas a este curso.")

    def mostrar_info(self):
        return f"|Id: {self.id_curso}|Nombre: {self.nombre}|Instructor: {self.instructor}|"

class Evaluacion:
    def __init__(self, id, descripcion, punteo):
        self.__id = id
        self.descripcion = descripcion
        self.punteo = punteo
        self.notas = {}

    def registrar_calificacion(self, estudiante, nota):
        self.notas[estudiante] = nota

    def mostrar_info(self):
        return f'|Id: {self.id}|Descripción: {self.descripcion}|Punteo: {self.punteo}|'

    @property
    def id(self):
        return self.__id