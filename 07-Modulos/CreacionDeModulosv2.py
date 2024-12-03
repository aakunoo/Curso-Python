# import CreacionDeModulos as cdm # as es para dar alias al modulo.

# cdm.sumar(10, 23)
# cdm.restar(5, 3)
# cdm.multiplicar(10, 6)


# Para importar solo una funcion de algun modulo, se hace de la siguiente manera:
# con un import * se importan todas las funciones del modulo.
from Paquetes.CalculosBasicos.CreacionDeModulos import sumar, restar
# from Paquetes.CalculosAdicionales.PotenciaYRedondeo import *

# Asi no hay necesidad de poner el nombre del modulo antes de la funcion.
sumar(5, 8)
restar(10, 3)

# potencia(2, 3)
