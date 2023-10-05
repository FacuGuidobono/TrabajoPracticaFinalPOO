import time
from clases.encargados import Encargado
from clases.profesores import Profesor
from clases.alumnos import Alumno
from modulos.decorators import *



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

# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

encargados = [ Encargado(random_name(),random_lastname(),random_dni()) for _ in range(10)] #creamos 10 encargados con valores random
profesores = [ Profesor(random_name(),random_lastname(), random_materia(),random_cursos(),random_div()) for _ in range(20)] # creamos 10 profesores con valores random
alumnos    = [ Alumno(random_name(),random_lastname(),random_materia(), random_cursos() ,random_div(),random_notas(),random_fecha(), " ", " ") for _ in range(30)] # creamos 20 alumno con valores random

for profesor in profesores:
     print(profesor.nombre,profesor.apellido,profesor.materia,profesor.curso,profesor.division)
     for alumno in alumnos:
          printc(f'\n{alumno.nombre} {alumno.apellido} {alumno.materia} {alumno.curso} {alumno.division}','red')
          if alumno.materia == profesor.materia and alumno.curso == profesor.curso and alumno.division == profesor.division:
               print('here')
               alumno.profesor_nombre = profesor.nombre
               alumno.profesor_apellido = profesor.apellido
               printc(f'\n{alumno.profesor_nombre} {alumno.profesor_apellido}','green')
              
for alumno in alumnos:
     printc(f'\n{alumno.profesor_nombre} {alumno.profesor_apellido}','green')
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
def crear_base_de_datos():
     
     
     with open('data/profesores.txt', 'w') as archivo:
     # Escribe el nombre en el archivo
          for profesor in profesores:
               profesor_data = profesor.nombre + ',' + profesor.apellido + ',' + profesor.materia + ',' + str(profesor.curso) + ',' + profesor.division + '\n'
               archivo.write(profesor_data)
     with open('data/encargados.txt', 'w') as archivo:
          for encargado in encargados:
               encargado_data = encargado.nombre + ',' + encargado.apellido + ',' + str(encargado.dni) + '\n'
               archivo.write(encargado_data)

     with open('data/alumnos.txt', 'w') as archivo:
          for alumno in alumnos:
               alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
               archivo.write(alumno_data)
     
crear_base_de_datos()