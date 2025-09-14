from abc import ABC, abstractmethod
from cursos import Evaluacion
from cursos import Curso
from usuarios import Estudiante, Instructor

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
        try:
            with open("data/usuarios.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        if linea.startswith('estudiante'):
                            rol, nombre, correo, fecha_nacimiento, id, carrera, cursos = linea.split(":")
                            if cursos:
                                lista_cursos = cursos.split(',')
                            else:
                                lista_cursos = []
                            self.usuarios[id] = Estudiante(nombre, correo, fecha_nacimiento, id, carrera)
                            self.usuarios[id].cursos = lista_cursos
                        elif linea.startswith('instructor'):
                            rol, nombre, correo, fecha_nacimiento, id, cursos_asignados = linea.split(":")
                            if cursos_asignados:
                                lista_cursos = cursos_asignados.split(',')
                            else:
                                lista_cursos = []
                            self.usuarios[id] = Instructor(nombre, correo, fecha_nacimiento, id)
                            self.usuarios[id].cursos_asignados = lista_cursos
            print("Usuarios importados desde usuarios.txt")
        except FileNotFoundError:
            print("No existe el archivo usuarios.txt, se creará uno nuevo al guardar.")

    def guardar_datos(self):
        with open('data/usuarios.txt', 'w', encoding='utf-8') as archivo:
            for usuario in self.usuarios.values():
                if usuario.rol == 'estudiante':
                    archivo.write(f'{usuario.rol}:{usuario.nombre}:{usuario.correo}:{usuario.fecha_nacimiento}:{usuario.id}:{usuario.carrera}:{",".join(usuario.cursos)}\n')
                elif usuario.rol == 'instructor':
                    archivo.write(f'{usuario.rol}:{usuario.nombre}:{usuario.correo}:{usuario.fecha_nacimiento}:{usuario.id}:{",".join(usuario.cursos_asignados)}\n')


    def agregar_datos(self, usuario):
        if usuario.id not in self.usuarios:
            self.usuarios[usuario.id] = usuario
            self.guardar_datos()
            print('Usuario agregado correctamente.')
        else:
            print('Id ya registrado')

class DatosCursos(Datos):
    def __init__(self):
        self.cursos = {} # {id_curso: Curso}
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open("data/cursos.txt","r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_curso,nombre,instructor,estudiantes, evaluaciones= linea.split(":")
                        curso= Curso(id_curso,nombre,instructor)
                        if estudiantes:
                            lista_estudiantes = estudiantes.split(',')
                            for estudiante in lista_estudiantes:
                                curso.inscribir_estudiante(estudiante)
                        if evaluaciones:
                            lista_evaluaciones = evaluaciones.split(',')
                            for evaluacion in lista_evaluaciones:
                                curso.agregar_evaluacion(evaluacion)
                        self.cursos[curso.id_curso]=curso
            print("Cursos importados desde cursos.txt")
        except FileNotFoundError:
            print("No existe el archivo cursos.txt, se creará uno nuevo al guardar")

    def guardar_datos(self):
        with open("data/cursos.txt","w",encoding="utf-8") as archivo:
            for id_curso, curso in self.cursos.items():
                archivo.write(f"{curso.id_curso}:{curso.nombre}:{curso.instructor}:{",".join(curso.estudiantes)}:{",".join(curso.evaluaciones)}\n")

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
            with open("data/evaluaciones.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_eval, estatus, descripcion, punteo, notas = linea.split(":")
                        self.evaluaciones[id_eval] = Evaluacion(id_eval, estatus, descripcion, punteo)
                        if notas:
                            for par in notas.split(","):
                                id_est, nota = par.split("=")
                                self.evaluaciones[id_eval].notas[id_est] = int(nota)
            print("Evaluaciones importadas desde 'evaluaciones.txt'")
        except FileNotFoundError:
            print("No existe el archivo 'evaluaciones.txt', se creara uno al guardar. ")

    def guardar_datos(self):
        with open("data/evaluaciones.txt", "w", encoding="utf-8") as archivo:
            for evaluacion in self.evaluaciones.values():
                notas = []
                for est, nota in evaluacion.notas.items():
                    notas.append(f"{est}={nota}")
                notas_str = ",".join(notas)
                archivo.write(f"{evaluacion.id}:{evaluacion.estatus}:{evaluacion.descripcion}:{evaluacion.punteo}:{notas_str}\n")

    def agregar_datos(self, id_eval, estatus, descripcion, punteo):
        if id_eval in self.evaluaciones:
            print("Id ya registrado")
        else:
            self.evaluaciones[id_eval] = Evaluacion(id_eval, estatus, descripcion, punteo)
            self.guardar_datos()
            print('Evaluación agregada correctamente.')