from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, correo, fecha_nacimiento):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    @abstractmethod
    def mostrar_info(self):
        return f"|Nombre: {self.nombre}|Correo: {self.correo}|Año de nacimiento: {self.fecha_nacimiento}|"

class Estudiante(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, carnet, carrera):
        super().__init__(nombre, correo, fecha_nacimiento)
        self.__rol = 'estudiante'
        self.__carnet = carnet
        self.__carrera = carrera
        self.cursos=[]

    def mostrar_info(self):
        return 'ESTUDIANTE: ' + super().mostrar_info() + f"Carnet: {self.__carnet}|Carrera: {self.carrera}|"

    def acceder_sistema(self, cursos, evaluaciones, usuarios):
        print('ACCESO AL SISTEMA DE ESTUDIANTE\n')
        while True:
            print("1. Inscribirse en un curso.\n"
                  "2. Consultar mis cursos.\n"
                  "3. Ver mis evaluaciones.\n"
                  "4. Consultar mis calificaciones.\n"
                  "5. Volver a menu principal")
            option = input("Ingrese una opción: ")
            match option:
                case '1':
                    cursos.mostrar_datos()
                    curso_id = input('Ingrese el id del curso al que desea inscribirse: ')
                    if curso_id in cursos.cursos and curso_id not in self.cursos:
                        self.cursos.append(curso_id)
                        cursos.cursos[curso_id].inscribir_estudiante(self.id)
                        cursos.guardar_datos()
                        print(f'Te has inscrito al curso con id: {curso_id}')
                    else:
                        print('Curso inexistente o ya inscrito previamente.')

                case '2':
                    if self.cursos:
                        print('Cursos en los que estás inscrito:')
                        for i, id_curso in enumerate(self.cursos, 1):
                            print(f'{i}. {cursos.cursos[id_curso].mostrar_info()}')
                    else:
                        print('No estás inscrito a ningún curso.')

                case '3':
                    if self.cursos:
                        evaluaciones_est = {} # evaluaciones_est = {id_curso: [id_evaluacion1, id_evaluacion2]}
                        for id_curso in self.cursos:
                            if cursos.cursos[id_curso].evaluaciones:
                                evaluaciones_est[id_curso] = []
                                for id_evaluacion in cursos.cursos[id_curso].evaluaciones:
                                    evaluaciones_est[id_curso].append(id_evaluacion)
                        if evaluaciones_est:
                            for curso, evaluaciones_list in evaluaciones_est.items():
                                print(f'CURSO: {cursos.cursos[curso].nombre}')
                                for evaluacion in evaluaciones_list:
                                    print(f'EVALUACIÓN: {evaluaciones.evaluaciones[evaluacion].mostrar_info()}\n')
                                print()
                        else:
                            print('No tienes ninguna evaluación asignada.')
                    else:
                        print('No estás inscrito a ningún curso.')

                case '4':
                    if self.cursos:
                        calificaciones = {} # calificaciones = {id_curso: {id_evaluacion: nota}}
                        for id_curso in self.cursos:
                            if cursos.cursos[id_curso].evaluaciones:
                                calificaciones[id_curso] = {}
                                for id_evaluacion in cursos.cursos[id_curso].evaluaciones:
                                    if self.id in evaluaciones.evaluaciones[id_evaluacion].notas:
                                        calificaciones[id_curso][id_evaluacion] = evaluaciones.evaluaciones[id_evaluacion].notas[self.id]
                                    else:
                                        calificaciones[id_curso][id_evaluacion] = 'Sin nota asignada.'
                        if calificaciones:
                            for curso, evaluaciones_dict in calificaciones.items():
                                print(f'CURSO: {cursos.cursos[curso].nombre}')
                                for evaluacion, nota in evaluaciones_dict.items():
                                    print(f'EVALUACIÓN {evaluaciones.evaluaciones[evaluacion].id} - Nota: {nota}\n')
                                print()
                        else:
                            print('No tienes ninguna evaluación asignada.')
                    else:
                        print('No estás inscrito a ningún curso.')

                case '5':
                    break


    @property
    def id(self):
        return self.__carnet

    @property
    def carrera(self):
        return self.__carrera

    @property
    def rol(self):
        return self.__rol

class Instructor(Usuario):
    def __init__(self, nombre, correo, fecha_nacimiento, codigo_empleado):
        super().__init__(nombre, correo, fecha_nacimiento)
        self.__rol = 'instructor'
        self.__codigo_empleado = codigo_empleado
        self.cursos_asignados = []

    def mostrar_info(self):
        return 'INSTRUCTOR: ' +  super().mostrar_info()+f"|Codigo de empleado: {self.__codigo_empleado}|"

    def acceder_sistema(self, cursos, evaluaciones, usuarios):
        print('ACCESO AL SISTEMA DE INSTRUCTOR\n')
        while True:
            print("1. Consultar mis cursos asignados")
            print("2. Ver estudiantes inscritos")
            print("3. Crear evaluaciones")
            print("4. Registrar calificaciones")
            print('5. Volver a menu principal')
            opcion= input("Ingrese una de las opciones: ")
            match opcion:
                case "1":
                    if self.cursos_asignados:
                        print('--- Mis Cursos Asignados ---')
                        for i, id_curso in enumerate(self.cursos_asignados, 1):
                            print(f'{i}. {cursos.cursos[id_curso].mostrar_info()}')
                        print('----------------------------')
                    else:
                        print('No tienes cursos asignados.')

                case "2":
                    if not self.cursos_asignados:
                        print('No tienes cursos asignados para poder ver estudiantes.')
                        continue

                    print('--- Selecciona un curso para ver los estudiantes inscritos ---')
                    for i, id_curso in enumerate(self.cursos_asignados, 1):
                        print(f'{i}. {cursos.cursos[id_curso].nombre}')

                    try:
                        seleccion = int(input('Elige el número del curso: '))
                        curso_seleccionado_id = self.cursos_asignados[seleccion - 1]
                        curso_obj = cursos.cursos[curso_seleccionado_id]
                        curso_obj.ver_estudiantes_inscritos(usuarios)
                    except (ValueError, IndexError):
                        print('Selección no válida. Por favor, introduce un número de la lista.')

                case "3":
                    pass

                case '4':
                    pass

                case '5':
                    break


    @property
    def id(self):
        return self.__codigo_empleado

    @property
    def rol(self):
        return self.__rol