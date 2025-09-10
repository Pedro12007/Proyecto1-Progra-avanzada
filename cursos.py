class Cursos:
    def __init__(self, id, nombre, instructor, lista):
        self.__id = id
        self.nombre = nombre
        self.instructor = instructor
        self.__lista = lista
    def inscribir_estudiante(self):
        pass
    @property
    def id(self):
        return self.__id
    @property
    def lista(self):
        return self.__lista