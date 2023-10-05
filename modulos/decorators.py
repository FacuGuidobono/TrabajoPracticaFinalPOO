import os,time, sys, datetime
import random

###############################################################################################
#                                                                                             #
#  -----------  Códigos ANSI para cambiar el color del texto en la salida  ------------       #
#                                                                                             #
###############################################################################################
def printc(text: str = 'None', color: str='green', background: str=None, style: str=None) -> str: 
    styles = {
        "bold": "\033[1m",
        "underline": "\033[4m",
    }

    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "grey": "\033[90m",
        "black": "\033[30m",
        "reset": "\033[0m",
    }

    backgrounds = {
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "grey": "\033[47m",
        "reset": "\033[0m",
    }

    style_code = styles.get(style, "")
    color_code = colors.get(color, "")
    background_code = backgrounds.get(background, "")
    print(f"{background_code}{color_code}{style_code}{text}{colors['reset']}")
    


###############################################################################################
#                                                                                             #
#                       -----------   TITULO DEL PROGRAMA  ------------                       #
#                                                                                             #
###############################################################################################    
    
def print_box(text: str= 'None',color: str= 'green',style: str='bold') -> str:

    text_length = len(text)

    printc("+" + "-" * (text_length + 2) + "+", color, style)
    printc("|" + f" {text} ".center(text_length + 2) + "|",color,style)
    printc("+" + "-" * (text_length + 2) + "+", color, style)

###############################################################################################
#                                                                                             #
#                        -----------   LIMPIAR CONSOLA  ------------                          #
#                                                                                             #
###############################################################################################   

def clear_console(tiempo: float =1.2) -> None:
    time.sleep(tiempo)
    os.system("cls")

###############################################################################################
#                                                                                             #
#                        -----------   MENSAJE DE ERROR  ------------                         #
#                                                                                             #
############################################################################################### 
    
def msg_error(text: str= 'Opcion invalida!!!') -> None:
    time.sleep(1)   
    printc(f"{text}\n","red","yellow")
    msg_continuar()
    clear_console()
    
    
###############################################################################################
#                                                                                             #
#                     -----------   MENSAJE DE CONTINUAR  ------------                        #
#                                                                                             #
###############################################################################################   

def msg_continuar():
    if(input("\nPresione enter para continuar...")):
            clear_console() 
    


###############################################################################################
#                                                                                             #
#                     -----------   MENSAJE DE SALIR  ------------                            #
#                                                                                             #
###############################################################################################   

def msg_salir(mensaje: str = 'Saliendo...'):
    printc(mensaje, 'green', 'bold')
    clear_console() 
    




###############################################################################################
#                                                                                             #
#                         -----------   MENU PRINCIPAL  ------------                          #
#                                                                                             #
###############################################################################################   



# +++++++++++++++++++
# |      MENU       |  
# +++++++++++++++++++

def menu_principal(op: list, title: str = "MENU PRINCIPAL", salir: str = 'Salir') -> int:
    clear_console()
    
    op_len =len(op) #obtengo el numero de opciones
    
    print_box(f"    {title}   ","yellow")
    for i in range(op_len):
        
        printc(f"{i+1}. {op[i]}","green")
        
    printc(f"0. {salir}\n","green")
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion > op_len or opcion < 0:
            msg_error()
            menu_principal(op,title)
        clear_console()
        return opcion
    except ValueError:
        msg_error()
        clear_console()
        menu_principal(op,title)
        
###############################################################################################
#                                                                                             #
#                          -----------   VALIDACIONES  ------------                           #
#                                                                                             #
###############################################################################################   

def validar_un_input(text:str, tipo: callable) -> callable:
    try:
        if tipo == int:
            return int(input(text))
        elif tipo == float:
            return float(input(text))
        elif tipo == str:
            return str(input(text))
        else:
            ValueError
    except ValueError:
        msg_error()
        return validar_un_input(text,tipo)
#------------------------------------------------------------------------------ 
def validar_dos_input(text1: str, text2: str, tipo1: callable, tipo2: callable) -> int:
    try:
        #------------------------------------------------------------------------------    
        #Validacion de los tipos de dato que se ingresan en los inputs
        if tipo1 == int:
            if tipo2 == int:
                return int(input(text1)), int(input(text2))
            elif tipo2 == float:
                return int(input(text1)), float(input(text2))
            elif tipo2 == str:
                return int(input(text1)), str(input(text2))
        #------------------------------------------------------------------------------    
        elif tipo1 == float:
            if tipo2 == int:
                return float(input(text1)), int(input(text2))
            elif tipo2 == float:
                return float(input(text1)), float(input(text2))
            elif tipo2 == str:
                return float(input(text1)), str(input(text2))
        #------------------------------------------------------------------------------    
        elif tipo1 == str:
            if tipo2 == int:
                return str(input(text1)), int(input(text2))
            elif tipo2 == float:
                return str(input(text1)), float(input(text2))
            elif tipo2 == str:
                return str(input(text1)), str(input(text2))
        #------------------------------------------------------------------------------
        else:
            ValueError
    except ValueError:
        msg_error()
        return validar_dos_input(text1, text2, tipo1,tipo2)
    

###############################################################################################
#                                                                                             #
#                          -----------   Datos Random Para Usar  ------------                 #
#                                                                                             #
############################################################################################### 


def random_name(sexo: str = None) -> str:

    nombres_mujeres = ['Maria', 'Ana', 'Laura', 'Sandra', 'Elena', 'Sofia', 'Isabel', 'Marina', 'Analia', 'Laura', 'Dora', 'Camila', 'Micaela', 'Luciana', 'Marisa']
    nombres_hombres = ['Juan', 'Pedro', 'Marcos', 'Carlos', 'Manuel', 'Jorge', 'Pablo', 'Daniel', 'Javier', 'Marcos', 'Carlos', 'Manuel', 'Jorge', 'Pablo', 'Daniel']
   
    if sexo == None:
        num = random.randint(1,2)
        if num == 1:
               return random_name('F')
        elif num == 2:
               return random_name('M')
            
    elif sexo.upper() == 'F':
        return random.choice(nombres_mujeres)
    elif sexo.upper() == 'M':
        return random.choice(nombres_hombres)
    
        

def random_lastname() -> str:
    apellidos = ['Perez','Gomez','Martinez','Lopez','Gutierrez','Molina','Rodriguez','Hernandez',
                     'Herrera','Carrasco','Gonzalez','Fernandez','Perez','Lopez','Gomez','Martinez',
                     'Rodriguez','Hernandez','Herrera','Carrasco','Gonzalez','Fernandez','Perez','Lopez']
    return random.choice(apellidos)
        

def random_dni():
    return random.randint(100000000,999999999)

def random_age(inicial: int = 10, final: int = 80) -> int:
    return random.randint(inicial,final)

def random_cursos() -> int:
    return random.randint(1,6)

def random_div() -> str:
    div = ['A','B','C','D','E','F']
    return random.choice(div)

def random_materia() -> str:
    materia = ['Matematicas','Lengua','Historia','Ingles','Fisica','Quimica']
    return random.choice(materia)

def random_notas() -> int:
    return random.randint(-1,10)

def random_fecha() -> str:
    return datetime.date.today().strftime("%d/%m/%Y")


###############################################################################################
#                                                                                             #
#                       -----------   UNA SIMPLE BARRA DE CARGA  ------------                 #
#                                                                                             #
############################################################################################### 




def barra_de_carga(total: int = 100) -> None :
       
    for i in range(total + 1):
    
        time.sleep(0.04)
        longitud_barra = 50
        progreso = i / total
        caracteres_cargados = int(longitud_barra * progreso)
        barra = "[" + "=" * caracteres_cargados + " " * (longitud_barra - caracteres_cargados) + "]"
        sys.stdout.write(f"\r{barra} {int(progreso * 100)}%")
        sys.stdout.flush()
    