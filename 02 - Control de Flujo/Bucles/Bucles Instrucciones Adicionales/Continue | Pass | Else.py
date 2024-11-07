# Continue sirve que cuando el flujo de ejecucion llega a esta instruccion, se salta el resto del bucle y se va a la siguiente iteracion

nombre = "Jeronimo Vicente"

print(len(nombre))

contador = 0

for i in nombre:

    if i == " ":
        # Esto hace (en este caso) que cuando se encuentre un espacio en blanco se salte esa vuelta del bucle y se vaya a la siguiente
        continue

    contador += 1

print(contador)

# ----------------------------- Pass -----------------------------

# Pass es una instruccion que no hace nada, se usa para cuando se necesita una instruccion pero no se quiere hacer nada

nombre = ("Laura Lopez")
contador = 0

for i in nombre:

    pass

print(contador)

# ----------------------------- Else -----------------------------

email = input("Introduce tu email: ")

for i in email:

    if i == "@":
        arroba = True
        break

else:
    arroba = False

print(arroba)
