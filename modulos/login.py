from modulos.decorators import *


def login():
    titulo = 'Login'
    opciones = ['Encargados', 'Profesores']
    
    match(menu_principal(opciones, titulo)):
        case 0:
            login_encargados()
        case 1:
            login_profesores()
        case _:
            msg_error()
            return login()
       
    
            

def login_encargados():
    pass

def login_profesores():
    pass    