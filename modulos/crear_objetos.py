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

# #creamos 10 encargados con valores random
encargados = [ Encargado(random_name(),random_lastname(),random_dni()) for _ in range(10)]
profesores = [ Profesor(random_name(),random_lastname(), random_materia(),random_cursos(),random_div()) for _ in range(15)]
alumnos    = [ Alumno(random_name(),random_lastname(),random_materia(),random_cursos(),random_div(),random_notas(),random_fecha()) for _ in range(20)]

def crear_base_de_datos():
     
     
     with open('data/profesores.txt', 'w') as archivo:
     # Escribe el nombre en el archivo
          for profesor in profesores:
               nombre = profesor.nombre + ',' + profesor.apellido + ',' + profesor.materia + ',' + str(profesor.curso) + ',' + profesor.division + '\n'
               archivo.write(nombre)
     with open('data/encargados.txt', 'w') as archivo:
          for encargado in encargados:
               nombre = encargado.nombre + ',' + encargado.apellido + ',' + str(encargado.dni) + '\n'
               archivo.write(nombre)

     with open('data/alumnos.txt', 'w') as archivo:
          for alumno in alumnos:
               nombre = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + '\n'
               archivo.write(nombre)
     print_box('                                                 SISTEMA DE INSCRIPCIÓN A EXÁMENES                                                   ', 'green')
     printc('Por Favor, Espere Mientras Se Carga La Base De Datos..\n','yellow')
     barra_de_carga()
     clear_console()
     print_box('                                                 SISTEMA DE INSCRIPCIÓN A EXÁMENES                                                   ', 'green')
     printc('\n\n - Base de Datos Cargada Exitosamente !!\n','green')
     time.sleep(0.2)
