from clases.profesores import Encargado
'''
+------------------------------------+
|                                    |                
|                                    |    
|           CLASE ALUMNO             |
|                                    |   
|                                    |   
+------------------------------------+
'''

class Alumno(Encargado):
    def __init__(self, nombre, apellido, materia, curso, division, nota: int= -1, fecha : str = '01/01/01'):
        super().__init__(nombre, apellido, materia, curso, division)
        self.__nota = nota
        self.__fecha = fecha
        
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
        
    def __eq__(self, otro):
        if isinstance(otro, Alumno):
            return self.nombre == otro.nombre and self.apellido == otro.apellido and self.materia == otro.materia and self.curso == otro.curso and self.division == otro.division and self.nota == otro.nota
        return False