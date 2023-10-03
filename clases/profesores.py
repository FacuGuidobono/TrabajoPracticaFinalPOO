'''
+------------------------------------+
|                                    |                
|                                    |    
|           CLASE PROFESOR           |
|                                    |   
|                                    |   
+------------------------------------+
'''



class Profesor:
    def __init__(self, nombre: str = 'Default', apellido: str = 'Default', materia: str = 'Default', curso: int = 0, division: int = 0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__materia = materia
        self.__curso = curso
        self.__division = division
        
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre:str) -> None:
        self.__nombre = nombre
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido: str) -> None:
        self.__apellido = apellido
        
    @property
    def materia(self) -> str:
        return self.__materia
    
    @materia.setter
    def materia(self, materia:str) -> None:
        self.__materia = materia
        
    @property
    def curso(self) -> int:
        return self.__curso
    
    @curso.setter
    def curso(self, curso:int) -> None:
        self.__curso = curso
        
    @property
    def division(self) -> str:
        return self.__division



 
 