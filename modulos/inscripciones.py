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
        return                                                                                                                              #profesor
    for data in alumnos_data:    # Nombre         # Apellido       # Materia         # Curso      # Division     # Nota        # Fecha  #nombre  # apellido       
        alumnos.append(Alumno(data[1].lower(), data[2].lower(), data[3].lower(), int(data[4]), data[5].lower(), int(data[6]), data[0], data[7] , data[8]))
    return alumnos
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>





################################################################################################################################################################################################
def tabla_alumnos(alumnos: list, usuario: str = None) -> None:
    
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







################################################################################################################################################################################################
#<----------------------------------------------------------------------------------------------------------------------------------------------------------
def tabla_un_alumno(i: int, alumnos_profesor: list) -> None:
    clear_console()
    printc(f'''
+-------------------------------------------------------------------------------------------------------------+
|N°      |       FECHA         |       NOMBRE        |      APELLIDO       |       MATERIA       |     NOTA   |               
+-------------------------------------------------------------------------------------------------------------+ 
| {str(i + 1).center(3)}.   |   {alumnos_profesor[i].fecha.center(15)}   |   {alumnos_profesor[i].nombre.center(15)}   |   {alumnos_profesor[i].apellido.center(15)}   |   {alumnos_profesor[i].materia.center(15)}   |   {str(alumnos_profesor[i].nota).center(3)}      |
+-------------------------------------------------------------------------------------------------------------+                                                        ''','yellow')
##############################################################################################################







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
    
    clear_console()
    printc('Nota Modicicada Con Exito','green')
    clear_console()
    tabla_un_alumno(i, alumnos_profesor) #mostrar datos modificados
    msg_continuar()



    
    
################################################################################################################################################################################################





def menu_profesores(usuario: 'Profesor'):

    clear_console()
    continuar = True
    total_alumnos = desempaquetado_alumnos() # despaquetado de todos los alumnos inscriptos
    alumnos_profesor = []

    for alumno in total_alumnos:
        if alumno.materia == usuario.materia and alumno.division == usuario.division and alumno.curso == usuario.curso:
            alumnos_profesor.append(alumno)

    while continuar:
        op = menu_principal(['Modificar Notas'],'MENU PROFESORES',salir='Atras')
        if op == 1:

            tabla_alumnos(alumnos_profesor) #muestra los alumnos del profesor

            num = validar_un_input(' Ingrese el numero del alumno que desea modificar/agregar nota: ',int)

            if num > len(alumnos_profesor) and num <= 0:
                clear_console()
                msg_error("El numero ingresado no corresponde a ningun alumno")
                continuar = False
                return continuar
            
            mod_notas(num, alumnos_profesor, total_alumnos)
            clear_console()
            tabla_alumnos(alumnos_profesor)
            msg_continuar()
            return 
        
        if op == 0:
            continuar = False
            return continuar
       



