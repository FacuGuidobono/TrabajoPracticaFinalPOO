from modulos.decorators import *
from modulos.loginencargados import *
from modulos.loginprofesores import *


def login_sistema():
    titulo = 'LOGIN'.center(120)
    opciones = ['Encargados', 'Profesores']
    
    match(menu_principal(opciones, titulo, salir='Volver')):
        case 1:
            login_encargados()
       
        case 2:
            login_profesores()
        case 0:
            msg_salir('Volviendo al Menu Principal..')
            return 
       
    
            