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
from clases.profesores import Profesor  
from modulos.decorators import *


##########################   PROFESORES #####################################


'''
+-------------------------------------+
|                                     |                
|                                     |    
|      DESEMPAQUETADO DE ALUMNOS      |   
|                                     |
|                                     |            
+-------------------------------------+
'''
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
def desempaquetado_alumnos() -> list:
    
  
    alumnos_data = []
    alumnos = []
    nombre_archivo = "data/alumnos.txt"
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for line in archivo:
                alumnos_data.append(line.strip().split(","))
    except FileNotFoundError:
        printc(f"El archivo '{nombre_archivo}' no se encontró.",'red','yellow')
        return                                                                                                                              #profesor
    for data in alumnos_data:    # Nombre         # Apellido       # Materia         # Curso      # Division     # Nota        # Fecha  #nombre  # apellido       
        alumnos.append(Alumno(data[1].lower(), data[2].lower(), data[3].lower(), int(data[4]), data[5].lower(), int(data[6]), data[0], data[7] , data[8]))
    return alumnos
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>





'''
+-------------------------------------+
|                                     |                
|                                     |    
|         TABLA DE ALUMNOS            |   
|                                     |
|                                     |            
+-------------------------------------+
'''
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
+-------------------------------------------------------------------------------------------------------------+ ''','green')


# <------------------------------------------------------------------------------------------------------------------------------------------------------------>


'''
+-------------------------------------+
|                                     |                
|                                     |    
|   TABLA QUE MUESTRA UN SOLO ALUMNO  |   
|                                     |
|                                     |            
+-------------------------------------+
'''
def tabla_un_alumno(i: int, alumnos_profesor: list) -> None:
    clear_console()
    printc(f'''
+-------------------------------------------------------------------------------------------------------------+
|N°      |       FECHA         |       NOMBRE        |      APELLIDO       |       MATERIA       |     NOTA   |               
+-------------------------------------------------------------------------------------------------------------+ 
| {str(i + 1).center(3)}.   |   {alumnos_profesor[i].fecha.center(15)}   |   {alumnos_profesor[i].nombre.center(15)}   |   {alumnos_profesor[i].apellido.center(15)}   |   {alumnos_profesor[i].materia.center(15)}   |   {str(alumnos_profesor[i].nota).center(3)}      |
+-------------------------------------------------------------------------------------------------------------+                                                        ''','yellow')


# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

'''
+-------------------------------------+
|                                     |                
|                                     |    
|         TABLA DE ALUMNOS            |   
|                                     |
|                                     |            
+-------------------------------------+
'''
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

def tabla_alumnos_encargado(alumnos: list) -> None:
    
    j = 1
    printc(f'''
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|N°      |       FECHA         |       NOMBRE        |      APELLIDO       |       MATERIA       |       CURSO     |     DIVISION    |       NOTA       |              PROFESOR             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ ''','yellow')
    for alumno in alumnos:

        printc(f'''
| {str(j).center(3)}.   |   {alumno.fecha.center(15)}   |   {alumno.nombre.center(15)}   |   {alumno.apellido.center(15)}   |   {alumno.materia.center(15)}   | {str(alumno.curso).center(15)} | {alumno.division.center(15)} | {  str(alumno.nota).center(15)}  |  {alumno.profesor_nombre.center(15)} {alumno.profesor_apellido.center(15)}  |''')
        j+=1
    printc(f'''
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ ''','green')


# <------------------------------------------------------------------------------------------------------------------------------------------------------------>


'''
+-------------------------------------+
|                                     |                
|                                     |    
|   TABLA QUE MUESTRA UN SOLO ALUMNO  |   
|                                     |
|                                     |            
+-------------------------------------+
'''
def tabla_un_alumno_encargado(i: int, alumnos_profesor: list) -> None:
    clear_console()
    printc(f'''
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|N°      |       FECHA         |       NOMBRE        |      APELLIDO       |       MATERIA       |       CURSO     |     DIVISION    |       NOTA       |              PROFESOR             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+  
| {str(i + 1).center(3)}.   |   {alumnos_profesor[i].fecha.center(15)}   |   {alumnos_profesor[i].nombre.center(15)}   |   {alumnos_profesor[i].apellido.center(15)}   |   {alumnos_profesor[i].materia.center(15)}   | {str(alumnos_profesor[i].curso).center(15)} | {alumnos_profesor[i].division.center(15)} | {  str(alumnos_profesor[i].nota).center(15)}  |  {alumnos_profesor[i].profesor_nombre.center(15)} {alumnos_profesor[i].profesor_apellido.center(15)}  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+    ''','yellow')


# <------------------------------------------------------------------------------------------------------------------------------------------------------------>




'''
+-------------------------------------+
|                                     |                
|                                     |    
|    MODIFICAR NOTAS  DE ALUMNOS      |   
|                                     |
|                                     |            
+-------------------------------------+
'''



def mod_notas(num: int, alumnos_profesor: list, total_alumnos: list) -> None:
    i = num -1
    tabla_un_alumno(i, alumnos_profesor)
    

    nueva_nota = validar_un_input(' Ingrese la nueva nota: ',int)
    
    if nueva_nota > 10 or nueva_nota < 0: # nota valida
        clear_console()
        msg_error("La nota ingresada no es valida")
        return

    #tengo que abrir el archivo alumnos.txt y actualizar la nota

    with open('data/alumnos.txt', 'w') as archivo:
          for alumno in total_alumnos:
               if alumnos_profesor[i] == alumno:
                   alumno.nota = nueva_nota
               alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
               archivo.write(alumno_data)
    
    printc('Modificando Nota del Alumno..\n','yellow')
    barra_de_carga()
    clear_console()
    print('\n')
    time.sleep(0.2)
    printc('Nota Modificada Con Exito','green')
    msg_continuar()
    return total_alumnos
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

'''
+-------------------------------------------+
|                                           |                
|                                           |    
|  ELIMINAR NOTA ALUMNO DE LA BASE DE DATOS |   
|                                           |
|                                           |            
+-------------------------------------------+
'''
def delete_nota(num: int, alumnos_profesor: list, total_alumnos: list) -> None:
    clear_console()
    
   
    
    i = num -1
    tabla_un_alumno(i, alumnos_profesor)

    printc('Eliminando Nota del Alumno..\n','yellow')
    barra_de_carga()
    clear_console()
    print('\n')
    time.sleep(0.2)

    with open('data/alumnos.txt', 'w') as archivo:
        
        for alumno in total_alumnos:

                if alumnos_profesor[i] == alumno:
                    alumno.nota = -1
                alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
                archivo.write(alumno_data)
    clear_console()    
    printc('Nota eliminada Con Exito','green')
  
    return total_alumnos

# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
      
def y(alumnos_profesor: list, total_alumnos:  list, func: callable, txt_validar: str = 'Default') -> None:  #str = 'Default'
    
    tabla_alumnos(alumnos_profesor) #muestra los alumnos del profesor

    num = validar_un_input(txt_validar,int)  #' Ingrese el numero del alumno que desea Modificar/Eliminar: '

    if 0 <= num <= len(alumnos_profesor):
            
        mod_tabla_alumnos = func(num, alumnos_profesor, total_alumnos)
            
        clear_console()
            
        tabla_alumnos_encargado(mod_tabla_alumnos)
        
        msg_continuar()
        
        
    else:
        clear_console()
        msg_error("El numero ingresado no corresponde a ningun alumno")
        return menu_encargados()
        
    
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>    
    
'''
+-------------------------------------+
|                                     |                
|                                     |    
|          MENU DE PROFESORES         |   
|                                     |
|                                     |            
+-------------------------------------+
'''



def menu_profesores(usuario: 'Profesor'):

    clear_console()
    
    total_alumnos = desempaquetado_alumnos() # despaquetado de todos los alumnos inscriptos
    alumnos_profesor = []

    for alumno in total_alumnos:
        if alumno.materia == usuario.materia and alumno.division == usuario.division and alumno.curso == usuario.curso:
            alumnos_profesor.append(alumno)
    
    
    
    op = menu_principal(['Modificar Notas', 'Eliminar Notas'],'MENU PROFESORES',salir='Atras')
    
    if op == 1:
        
        y(alumnos_profesor,total_alumnos,mod_notas,'Ingrese el N° de Alumno que quiere Modificar la Nota: ')    
        clear_console()
        return menu_profesores(usuario)

    elif op == 2: 
        y(alumnos_profesor,total_alumnos,delete_nota,'Ingrese el N° de Alumno que quiere Eliminar la Nota: ')    
        clear_console()       
        return menu_profesores(usuario)
        
    elif op == 0:
        return
        
        
        
        
        
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>      


########################## ENCARGADOS ###########################################



'''
+-------------------------------------+
|                                     |                
|                                     |    
| AGREGAR ALUMNOS A LA BASE DE DATOS  |   
|                                     |
|                                     |            
+-------------------------------------+
'''

def add_alumnos(total_alumnos: list) -> None:
    tabla_alumnos_encargado(total_alumnos)
    msg_continuar()
    clear_console()
    print_box('AGREGAR ALUMNO'.center(120,' '), 'green')
    
    with open('data/alumnos.txt', 'a') as archivo:
        

                    alumno = Alumno(validar_un_input('Ingrese el nuevo nombre: ',str), validar_un_input('Ingrese el nuevo apellido: ',str), validar_un_input('Ingrese la nueva materia: ',str), validar_un_input('Ingrese el nuevo curso: ',int),validar_un_input('Ingrese la nueva division: ',str),-1,validar_un_input('Ingrese la nueva fecha de inscripcion dd/mm/aaaa: ',str), validar_un_input('Ingrese el nombre del nuevo profesor: ',str), validar_un_input('ingrese el apellido del nuevo profesor: ',str))
                    alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
                    archivo.write(alumno_data)
    printc('Agregando Alumno..\n','yellow')
    barra_de_carga()
    clear_console()
    print('\n')
    clear_console()
    mod_tabla_alumnos = desempaquetado_alumnos()
    tabla_alumnos_encargado(mod_tabla_alumnos)               
    printc('Alumno Agregado Con Exito','green')       
    msg_continuar()
    
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

'''
+-------------------------------------+
|                                     |                
|                                     |    
|MODIFICAR ALUMNOS DE LA BASE DE DATOS|   
|                                     |
|                                     |            
+-------------------------------------+
'''
def mod_alumnos(num: int, total_alumnos: list) -> None:

    i = num -1
    tabla_un_alumno_encargado(i, total_alumnos)
    nuevos_datos_alumno = Alumno(validar_un_input('Ingrese el nuevo nombre: ',str), validar_un_input('Ingrese el nuevo apellido: ',str), validar_un_input('Ingrese la nueva materia: ',str), validar_un_input('Ingrese el nuevo curso: ',int),validar_un_input('Ingrese la nueva division: ',str),-1,validar_un_input('Ingrese la nueva fecha de inscripcion dd/mm/aaaa: ',str), validar_un_input('Ingrese el nombre del nuevo profesor: ',str), validar_un_input('ingrese el apellido del nuevo profesor: ',str))
    total_alumnos[i] = nuevos_datos_alumno
    printc('Modificando  Alumno..\n','yellow')
    barra_de_carga()
    clear_console()
    print('\n')
    
    
    with open('data/alumnos.txt', 'w') as archivo:
          for alumno in total_alumnos:   
                alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
                archivo.write(alumno_data)
    printc('Alumno Modificado Con Exito','green')            
    return total_alumnos

# <------------------------------------------------------------------------------------------------------------------------------------------------------------>

'''
+-------------------------------------+
|                                     |                
|                                     |    
| ELIMINAR ALUMNOS DE LA BASE DE DATOS|   
|                                     |
|                                     |            
+-------------------------------------+
'''
def delete_alumno(num: int, total_alumnos: list) -> None:
    clear_console()
    
   
    
    i = num -1
    tabla_un_alumno_encargado(i, total_alumnos)
    del total_alumnos[i]
    printc('Eliminando Alumno..\n','yellow')
    barra_de_carga()
    clear_console()
    print('\n')
    
    time.sleep(0.2)
   
    with open('data/alumnos.txt', 'w') as archivo:
        
        for alumno in total_alumnos:
               
                alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
                archivo.write(alumno_data)
    clear_console()    
    printc('Alumno eliminado Con Exito','green')
  
    return total_alumnos

# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
      
def x(total_alumnos: list, func: callable, txt_validar: str = 'Default') -> None:  #str = 'Default'
    
    tabla_alumnos_encargado(total_alumnos)

    num = validar_un_input(txt_validar,int)  #' Ingrese el numero del alumno que desea Modificar/Eliminar: '

    if 0 <= num <= len(total_alumnos):
            
        mod_tabla_alumnos = func(num, total_alumnos)
            
        clear_console()
            
        tabla_alumnos_encargado(mod_tabla_alumnos)
        
        msg_continuar()
        
        
    else:
        clear_console()
        msg_error("El numero ingresado no corresponde a ningun alumno")
        return menu_encargados()
        
    
# <------------------------------------------------------------------------------------------------------------------------------------------------------------> 

    
'''
+-------------------------------------+
|                                     |                
|                                     |    
|          MENU DE ENCARGADOS         |   
|                                     |
|                                     |            
+-------------------------------------+
'''

def menu_encargados():
    
    total_alumnos = desempaquetado_alumnos() # despaquetado de todos los alumnos inscriptos
    
    op = menu_principal(['Agregar Almuno','Modificar Alumno','Eliminar Alumno'],'MENU ENCARGADOS',salir='Atras')
    
    
    
    if op == 1:

        add_alumnos(total_alumnos)
        return menu_encargados()
            
    elif op == 2:
        
        x(total_alumnos, mod_alumnos, 'Modificar Alumno del Sistema: ')
        clear_console()
        return menu_encargados()
    elif op == 3:
        x(total_alumnos, delete_alumno, 'Eliminar Alumno del Sistema: ')
        clear_console()
        return menu_encargados()
                             
            
    elif op == 0:
          return
        
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>