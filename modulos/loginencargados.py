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


def desempaquetado_encargados():
    
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
    printc('Por Favor, Espere Mientras Se Carga La Base De Datos..\n','yellow')
    #barra_de_carga()
    clear_console()
    print('\n')
    printc('Base de Datos Cargada Exitosamente !!'.center(120),color='white',background='green')
    time.sleep(0.2)
    clear_console()
# <------------------------------------------------------------------------------------------------------------------------------------------------------------>
    
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
    
    ingreso = Encargado(nombre.lower(), apellido.lower(), int(dni))
    #printc(f'{ingreso.nombre} {ingreso.apellido} {ingreso.dni}',background='green')
    
    for encargados in encargados:
       # printc(f'{encargados.nombre} {encargados.apellido} {encargados.dni}','red')
        if encargados == ingreso:
            printc('-'.center(120),'cyan', background='green')
            print('BIENVENIDO ENCARGADO'.center(120))
            printc('-'.center(120),'cyan', background='green')
            msg_continuar()
            return 'encargado'
        else: 
            print('Datos Incorrectos !!!')
            return

#########################################################################          
#login_encargados()
