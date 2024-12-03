nombre = input("Introce tu nombre: ")

# upper() convierte el texto a mayúsculas
print("El nombre introducido es: ", nombre.upper())

# capitalize() convierte la primera letra a mayuscula.
print("El nombre introducido es: ", nombre.capitalize())

'''
Ejemplo mas practico

Nos piden introducir un valor numerico y no queremos que el usuario introduzca un texto.
'''

numero = input("Introduce un número: ")

# isdigit() comprueba si el valor introducido es un número
while (numero.isdigit() == False):
    numero = input("Introduce un número: ")

print("Has introducido el número: ", numero)

cadena = "  Esto es una cadena de texto, amo a mi novia.  "

# center() hace que la cadena se centre en la consola con el numero de caracteres que le indiquemos
print(cadena.center(80, "-"))

# swapcase() intercambia las mayusculas por minusculas y viceversa
print(cadena.swapcase())

# strip() elimina los espacios en blanco al principio y al final de la cadena
print(cadena.strip())

# split() divide la cadena en una lista de palabras
print(cadena.split())

# https://pyspanishdoc.sourceforge.net/lib/string-methods.html
