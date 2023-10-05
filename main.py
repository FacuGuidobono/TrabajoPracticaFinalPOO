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
    #  crear_base_de_datos()   #crea los archivos txt necesarios para el funcionamiento del sistema si es que no existen con datos aleatorios
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






