from EjercicioModulo1 import *

while True:
    contra = input("Ingrese una contra: ")
    if validarContra(contra) == True:
        break
    else:
        print(validarContra(contra))
