'''
+------------------------------------+
|                                    |                
|                                    |    
|          CLASE ENCARGADO           |
|                                    |   
|                                    |   
+------------------------------------+
'''



class Encargado:
    def __init__(self, nombre: str = None, apellido: str = None, dni: int = 0000000):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
        
    @property
    def dni(self) -> int:
        return self.__dni  
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni






