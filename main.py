'''
+-------------------------------------+
|                                     |                
|                                     |    
|  Sistema de Inscripción a Exámenes  |
|                                     |   
|                                     |   
+-------------------------------------+
'''
from modulos.decorators import *
from modulos.login import *
#from modulos.crear_objetos import *



def login_sistema():
    titulo = 'LOGIN'.center(120)
    opciones = ['Encargados', 'Profesores']
    
    op = menu_principal(opciones, titulo, salir='Volver')
    
    
    if op ==  1:
            login_encargados()
    elif op == 2:
            login_profesores()
    elif 0:
            msg_salir('Volviendo al Menu Principal..')
       
    


def main() -> bool:
    #Descomentar parar rcrea los archivos con datos aleatorios txt necesarios 
    # para el funcionamiento del sistema si es que estos no existen.
    #crear_base_de_datos()
    
    title = 'SISTEMA DE INSCRIPCIÓN A EXÁMENES'.center(120,' ')
    match(menu_principal(['Ingreso al Sistema'], title)):
        case 1:
           login_sistema()
           return True
            
        case 0:
            return False
        
    
    
    


if __name__ == "__main__":
   
   continuar = True
   while continuar:
       continuar = main()  






