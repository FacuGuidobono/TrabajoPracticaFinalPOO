'''
+-------------------------------------+
|                                     |                
|                                     |    
|  SISTEMA DE INSCRIPCION A EXAMENES  |   
|  Encargados agregan/modif. alumnos  |   
|  Profesores agregan/modif. Notas    |   
|                                     |   
+-------------------------------------+
'''
from clases.alumnos import Alumno
from modulos.decorators import *

def desempaquetado_alumnos() -> list:
    
    # <------------------------------------------------------------------------------------------------------------------------------------------------------------>
    alumnos_data = []
    alumnos = []
    nombre_archivo = "data/alumnos.txt"
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for line in archivo:
                alumnos_data.append(line.strip().split(","))
    except FileNotFoundError:
        printc(f"El archivo '{nombre_archivo}' no se encontró.",'red','yellow')
        return
    for data in alumnos_data:    # Nombre         # Apellido       # Materia         # Curso      # Division     # Nota           # Fecha          
        alumnos.append(Alumno(data[1].lower(), data[2].lower(), data[3].lower(), int(data[4]), data[5].lower(), int(data[6]), data[0]))
    return alumnos
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

def tabla_alumnos(alumnos: list) -> None:
    
    j = 1
    printc(f'''
+-------------------------------------------------------------------------------------------------------------+
|N°      |       FECHA         |       NOMBRE        |      APELLIDO       |       MATERIA       |     NOTA   |               
+-------------------------------------------------------------------------------------------------------------+ ''','yellow')

    for alumno in alumnos:
        printc(f'''
| {str(j).center(3)}.   |   {alumno.fecha.center(15)}   |   {alumno.nombre.center(15)}   |   {alumno.apellido.center(15)}   |   {alumno.materia.center(15)}   |   {str(alumno.nota).center(3)}      |''')
        j+=1
    printc(f'''
+-------------------------------------------------------------------------------------------------------------+ ''')

def menu_encargado():
    pass






def sistema_de_inscripcion(usuario: str ) -> None: 
    
    if usuario == 'encargado':

        a = desempaquetado_alumnos()
        tabla_alumnos(a)
        
sistema_de_inscripcion()
