from clases.encargados import Encargado
from decorators import *


'''
+-------------------------------------+
|                                     |                
|                                     |    
|  Se Crean los objetos, Encargados,  |
|  Profesores y alumnos para ser      |   
|  guardados en la "base de datos".   |   
|                                     |   
|                                     |   
+-------------------------------------+
'''

# #creamos 10 encargados con valores random
encargados = [ Encargado(random_name('f'),random_lastname(),random_dni()) for _ in range(10)]

for _ in range(len(encargados)):
     print(encargados[_].nombre, encargados[_].apellido, encargados[_].dni)





