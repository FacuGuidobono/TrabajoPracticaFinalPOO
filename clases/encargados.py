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
    def __init__(self, nombre: str = 'Default', apellido: str = 'Default', dni: int = 0000000):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre.lower()
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido: str) -> None:
        self.__apellido = apellido.lower()
       
    @property
    def dni(self) -> int:
        return self.__dni  
    
    @dni.setter
    def dni(self, dni:int) -> None:
        self.__dni = dni

    def __eq__(self, otro):
        if isinstance(otro, Encargado):
            return self.nombre == otro.nombre and self.apellido == otro.apellido and self.dni == otro.dni   
        return False




