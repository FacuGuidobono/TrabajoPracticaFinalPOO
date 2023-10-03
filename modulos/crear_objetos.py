from clases.encargados import Encargado
from clases.profesores import Profesor
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
encargados = [ Encargado(random_name(),random_lastname(),random_dni()) for _ in range(10)]
profesores = [ Profesor(random_name(),random_lastname(), random_materia(),random_cursos(),random_div()) for _ in range(15)]

for _ in range(len(encargados)):
     print(encargados[_].nombre, encargados[_].apellido, encargados[_].dni)
     
printc('x'*50,'green')

for _ in range(len(profesores)):
     print(profesores[_].nombre, profesores[_].apellido, profesores[_].materia, profesores[_].curso, profesores[_].division)





