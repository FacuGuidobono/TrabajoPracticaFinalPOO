from modulos.decorators import *


def login_sistema():
    titulo = '                                      Login                                   '
    opciones = ['Encargados', 'Profesores']
    
    match(menu_principal(opciones, titulo)):
        case 1:
            login_encargados()
            return True
        case 2:
            login_profesores()
            return True
        case 0:
            msg_salir()
            return True
       
    
            

def login_encargados():
    printc('Bienvenido Encargado', 'green')
    msg_continuar()

def login_profesores():
    printc('Bienvenido Profesor', 'green')
    msg_continuar()   