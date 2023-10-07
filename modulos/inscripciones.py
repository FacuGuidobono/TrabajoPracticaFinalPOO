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
    
    
    printc('Nota Modicicada Con Exito','green')
    #tabla_un_alumno(i, alumnos_profesor) #mostrar datos modificados
    msg_continuar()

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
    continuar = True
    total_alumnos = desempaquetado_alumnos() # despaquetado de todos los alumnos inscriptos
    alumnos_profesor = []

    for alumno in total_alumnos:
        if alumno.materia == usuario.materia and alumno.division == usuario.division and alumno.curso == usuario.curso:
            alumnos_profesor.append(alumno)

    while True:
        op = menu_principal(['Modificar Notas'],'MENU PROFESORES',salir='Atras')
        if op == 1:

            tabla_alumnos(alumnos_profesor) #muestra los alumnos del profesor

            num = validar_un_input(' Ingrese el numero del alumno que desea modificar/agregar nota: ',int)

            if num > len(alumnos_profesor) and num <= 0:
                clear_console()
                msg_error("El numero ingresado no corresponde a ningun alumno")
                
            
            mod_notas(num, alumnos_profesor, total_alumnos)
            clear_console()
            tabla_alumnos(alumnos_profesor)
            msg_continuar()
            
        
        if op == 0:
            break
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>      

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
    
    with open('data/alumnos.txt', 'w') as archivo:
          for alumno in total_alumnos:
                if total_alumnos[i] == alumno:
                    total_alumnos[i] = Alumno(validar_un_input('Ingrese el nuevo nombre: ',str), validar_un_input('Ingrese el nuevo apellido: ',str), validar_un_input('Ingrese la nueva materia: ',str), validar_un_input('Ingrese el nuevo curso: ',int),validar_un_input('Ingrese la nueva division: ',str),-1,validar_un_input('Ingrese la nueva fecha de inscripcion dd/mm/aaaa: ',str), validar_un_input('Ingrese el nombre del nuevo profesor: ',str), validar_un_input('ingrese el apellido del nuevo profesor: ',str))
                alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
                archivo.write(alumno_data)
    mod_total_alumnos = desempaquetado_alumnos()
    clear_console()
    tabla_alumnos_encargado(mod_total_alumnos)
    printc('Alumno Modificado Con Exito','green')
    msg_continuar()   

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
    
    i = num -1
    tabla_un_alumno_encargado(i, total_alumnos)
   
                
    
    with open('data/alumnos.txt', 'w') as archivo:
          for alumno in total_alumnos:
                if total_alumnos[i] == alumno:
                    del total_alumnos[i]
                alumno_data = alumno.fecha + ','+ alumno.nombre + ',' + alumno.apellido + ',' + alumno.materia + ',' + str(alumno.curso) + ',' + alumno.division + ',' + str(alumno.nota) + ',' + alumno.profesor_nombre + ',' + alumno.profesor_apellido + '\n'
                archivo.write(alumno_data)
    mod_tabla_alumnos = desempaquetado_alumnos()
    tabla_alumnos_encargado(mod_tabla_alumnos)
    printc('Alumno Eliminado Con Exito','green')
    msg_continuar()

# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
      
def x(total_alumnos: list, func: callable, txt_validar: str = 'Default') -> None:  #str = 'Default'
    
    tabla_alumnos_encargado(total_alumnos)

    num = validar_un_input(txt_validar,int)  #' Ingrese el numero del alumno que desea Modificar/Eliminar: '

    if num <= len(total_alumnos) and num > 0:
        
        func(num, total_alumnos)
        
        clear_console()
        
        tabla_alumnos_encargado(total_alumnos)
        
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
        return menu_encargados()
    elif op == 3:
        x(total_alumnos, delete_alumno, 'Eliminar Alumno del Sistema: ')
        return menu_encargados() # 05/10/2023,micaela,hernandez,quimica,1,a,4,Luciana,Lopez
                                 # 05/10/2023,daniel,herrera,quimica,1,a,4,Luciana,Lopez
            
    elif op == 0:
          return
        
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>