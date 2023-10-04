'''
+-------------------------------------+
|                                     |                
|                                     |    
|  Se lee la base de datos , se       |
|  desempaquetan los datos de los     |   
|  profesores y se crean los objetos  |   
|  profesores para relizar el login   |   
|                                     |   
+-------------------------------------+
'''

from modulos.decorators import *
from clases.profesores import Encargado

def desempaquetado_profesores():
    
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
    printc('Por Favor, Espere Mientras Se Carga La Base De Datos..\n','yellow')
    #barra_de_carga()
    clear_console()
    print('\n')
    printc('Base de Datos Cargada Exitosamente !!'.center(120),color='white',background='green')
    time.sleep(0.2)
    clear_console()
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
    
    profesores_data = []
    profesores = []
    nombre_archivo = "data/profesores.txt"
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for line in archivo:
                profesores_data.append(line.strip().split(","))
    except FileNotFoundError:
        printc(f"El archivo '{nombre_archivo}' no se encontró.",'red','yellow')
        
        login_profesores()
    for data in profesores_data:
        profesores.append(Encargado(data[0].lower(), data[1].lower(), data[2].lower(), int(data[3]), data[4].lower()))
    return profesores
#####################################################################################################################
def login_profesores():   
    
    profesores = desempaquetado_profesores()
    
    print_box('Login Profesores'.center(120),'green')
    
    nombre, apellido = validar_dos_input('Ingrese su nombre: ', 'Ingrese su apellido: ', str,str)
    materia, curso = validar_dos_input('Ingrese su materia: ', 'Ingrese su curso: ', str,int)
    division = validar_un_input('Ingrese su division: ', str)
    
    ingreso = Encargado(nombre.lower(), apellido.lower(), materia.lower(), curso, division.lower())
    printc(f'{ingreso.nombre} {ingreso.apellido} {ingreso.materia} {ingreso.curso} {ingreso.division}',background='green')
    
    for profesor in profesores:
        printc(f'{profesor.nombre} {profesor.apellido} {profesor.materia} {profesor.curso} {profesor.division}','red')
        if profesor == ingreso:
            printc('Bienvenido !!!'.center(120),'green')
            return
        else: 
            print('Datos Incorrectos !!!')
            
login_profesores()
