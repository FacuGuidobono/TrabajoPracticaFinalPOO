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
from django.contrib.auth import login

#crear_base_de_datos()


def main() -> bool:
    title = 'SISTEMA DE INSCRIPCIÓN A EXÁMENES'.center(150,' ')
    match(menu_principal(['Login'], title)):
        case 1:
           login_sistema()
           return True
            
        case 0:
            return False
        
    
    
    


if __name__ == "__main__":
   continuar = True
   while continuar:
       continuar = main()  






