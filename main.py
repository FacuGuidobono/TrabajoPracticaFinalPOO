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
from modulos.crear_objetos import *
from modulos.login import *


 


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






