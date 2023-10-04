'''
+------------------------------------+
|                                    |                
|                                    |    
|           CLASE PROFESOR           |
|                                    |   
|                                    |   
+------------------------------------+
'''



class Encargado:
    def __init__(self, nombre: str = 'Default', apellido: str = 'Default', materia: str = 'Default', curso: int = 0, division: str = 'A'):
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
        self.__nombre = nombre.lower()
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido: str) -> None:
        self.__apellido = apellido.lower()
        
    @property
    def materia(self) -> str:
        return self.__materia
    
    @materia.setter
    def materia(self, materia:str) -> None:
        self.__materia = materia.lower()
        
    @property
    def curso(self) -> int:
        return self.__curso
    
    @curso.setter
    def curso(self, curso:int) -> None:
        self.__curso = curso
        
    @property
    def division(self) -> str:
        return self.__division
    @division.setter
    def division(self, division:str) -> None:
        self.__division = division.lower()

    def __eq__(self, otro):
        if isinstance(otro, Encargado):
            return self.nombre == otro.nombre and self.apellido == otro.apellido and self.materia == otro.materia and self.curso == otro.curso and self.division == otro.division
        return False

 
 