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




def main():
    title = 'SISTEMA DE INSCRIPCIÓN A EXÁMENES'.center(150,' ')
    match(menu_principal(['Login'], title)):
        case 1:
            return login_sistema()
            
        case 0:
            return False
        
    #crear_base_de_datos()
    
    


if __name__ == "__main__":
   continuar = True
   while continuar:
       continuar = main()  






