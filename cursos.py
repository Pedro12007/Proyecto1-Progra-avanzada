class Cursos:
    def __init__(self, id, name, instructor, list):
        self.__id = id
        self.name = name
        self.instructor = instructor
        self.__list = list
    def inscribir_estudiante(self):
        pass
    def get_id(self):
        return self.__id
    def set_id(self, ID):
        self.__id = ID
    def get_list(self):
        return self.__list
    def set_list(self, list):
        self.__list = list