from clases.profesores import Profesor
'''
+------------------------------------+
|                                    |                
|                                    |    
|           CLASE ALUMNO             |
|                                    |   
|                                    |   
+------------------------------------+
'''

class Alumno(Profesor):
    def __init__(self, nombre, apellido, materia, curso, division, nota, fecha, profesor_nombre , profesor_apellido):
        super().__init__(nombre, apellido, materia, curso, division)
        self.__nota = nota
        self.__fecha = fecha
        self.__profesor_nombre = profesor_nombre
        self.__profesor_apellido = profesor_apellido
        
    @property
    def nota(self) -> int:
        return self.__nota
    
    @nota.setter
    def nota(self, nota:int) -> None:
        self.__nota = nota
    
    @property
    def fecha(self) -> str:
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha:str) -> None:
        self.__fecha = fecha
    
    @property
    def profesor_nombre(self) -> str:
            return self.__profesor_nombre
        
    @profesor_nombre.setter
    def profesor_nombre(self, profesor_nombre:str) -> None:
        self.__profesor_nombre = profesor_nombre
    
    @property
    def profesor_apellido(self) -> str:
        return  self.__profesor_apellido
    
    @profesor_apellido.setter
    def profesor_apellido(self, profesor_apellido:str) -> None:
        self.__profesor_apellido = profesor_apellido
    
    def __eq__(self, otro):
        if isinstance(otro, Alumno):
            return self.nombre == otro.nombre and self.apellido == otro.apellido and self.materia == otro.materia and self.curso == otro.curso and self.division == otro.division and self.nota == otro.nota and self.profesor_nombre == otro.profesor_nombre and self.profesor_apellido == otro.profesor_apellido
        return False