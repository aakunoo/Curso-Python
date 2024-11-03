''' Ejemplo sencillo bucle while '''

contador = 0
while contador <= 10:
    print("Vuelta " + str(contador))
    contador = contador + 1

print("Fin del programa.")

# ---------------------------- Ejemplo mas complejo ----------------------------

# Queremos un control de acceso. Para que una persona en funcion de su edad pueda acceder a algun sitio.

edad = int(input("Introduce tu edad: "))

''' Tengo que usar or y no and porque si uso and, digo que necesito las dos condiciones para que se cumpla 
el bucle y me muestre el mensaje y es una condiciones que no se pueden cumplir a la vez. '''

while edad <= 0 or edad >= 80:
    print("Edad no valida.")
    edad = int(input("Introduce tu edad: "))

print("Puedes pasar.\n" "Edad del usuario: " + str(edad))
