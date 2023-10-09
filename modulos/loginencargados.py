'''
+-------------------------------------+
|                                     |                
|                                     |    
|  Se lee la base de datos , se       |
|  desempaquetan los datos de los     |   
|  Encargados y se crean los objetos  |   
|  Encargados para relizar el login   |   
|                                     |   
+-------------------------------------+
'''

from modulos.decorators import *
from clases.encargados import Encargado
from modulos.inscripciones import *


#####################################################################################################################
def desempaquetado_encargados():

    
    encargados_data = []
    encargados = []
    nombre_archivo = "data/encargados.txt"
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            for line in archivo:
                encargados_data.append(line.strip().split(","))
    except FileNotFoundError:
        printc(f"El archivo '{nombre_archivo}' no se encontró.",'red','yellow')
        
        return
    for data in encargados_data:     # Nombre       # Apellido         # DNI
        encargados.append(Encargado(data[0].lower(), data[1].lower(), int(data[2])))
    return encargados
#####################################################################################################################

def login_encargados():   
    
    encargados = desempaquetado_encargados()
    print_box('LOGIN ENCARGADOS'.center(120),'red')
    
    nombre, apellido = validar_dos_input('Ingrese su nombre: ', 'Ingrese su apellido: ', str,str)

    dni = validar_un_input('Ingrese su DNI: ', int)
    
    usuario = Encargado(nombre.lower(), apellido.lower(), int(dni))
    
    
    for encargado in encargados:
        
        if encargado == usuario:
            clear_console()
            printc('-'.center(120),'cyan', background='green')
            print('BIENVENIDO ENCARGADO'.center(120))
            print(f'{usuario.nombre.upper()} {usuario.apellido.upper()}'.center(120))
            printc('-'.center(120),'cyan', background='green')
            time.sleep(1)
            clear_console()
            
            return menu_encargados()
        
        
        
        
    msg_error('Datos Incorrectos !!!')
    clear_console()
    return login_encargados()

#######################################################################################################################          
