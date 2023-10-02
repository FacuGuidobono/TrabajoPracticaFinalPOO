from clases.encargados import Encargado
from modulos.decorators import DatosFake
'''
+-------------------------------------+
|                                     |                
|                                     |    
|  Se Crean los objetos, Encargados,  |
|  Profesores y alumnos para ser      |   
|  guardados en la "base de datos".   |   
|                                     |   
|                                     |   
+-------------------------------------+
'''



fake = DatosFake() # Instanciamos la clase DatosFake para obtener nombres, apellidos y dni

encargados = [Encargado(fake.name(), fake.lastname(), fake.dni()) for i in range(10)] # creamos 10 instancias de encargado y las guardamos

print(encargados)




