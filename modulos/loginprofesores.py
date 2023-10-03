from modulos.decorators import *



def login_profesores():   

    nombre_archivo = "data/profesores.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            
            lineas = archivo.readlines()
    except FileNotFoundError:
        printc(f"El archivo '{nombre_archivo}' no se encontró.",'red','yellow')
        lineas = []

    # Imprime las líneas o realiza cualquier operación con la lista
    print('\n')
    print(lineas[0][0])
    print(lineas[1])
    print('\n')
    for linea in lineas:
        print(linea.strip())  # strip() elimina espacios en blanco y saltos de línea alrededor del texto
        msg_continuar()

login_profesores()