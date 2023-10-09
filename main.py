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
from modulos.loginencargados import *
from modulos.loginprofesores import *
#from modulos.crear_objetos import *



def login_sistema():
    
    title = 'SISTEMA DE INSCRIPCIÓN A EXÁMENES'.center(120,' ')
    opciones = ['Encargados', 'Profesores']
    
    op = menu_principal(opciones, title, salir='Salir')
    
    
    if op ==  1:
            login_encargados()
            return True
    elif op == 2:
            login_profesores()
            return True
    elif 0:
            msg_salir('Saliendo del Sistema..')
            time.sleep(1)
            return False 
       
    


def main() -> bool:
    #Descomentar parar rcrea los archivos con datos aleatorios txt necesarios 
    # para el funcionamiento del sistema si es que estos no existen.
    #crear_base_de_datos()
    
    
     return login_sistema()
    
    
    


if __name__ == "__main__":
   
   continuar = True
   while continuar:
       continuar = main()  






