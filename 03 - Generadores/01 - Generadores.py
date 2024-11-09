''' Usar yield en lugar de return en una función la convierte en un generador. '''

# Primero funcion tradicional


# def generarPares(limite):

#     numero = 1
#     numerosPares = []

#     while numero < limite:
#         numerosPares.append(numero*2)
#         numero += 1

#     return numerosPares

# numeroIntroducido = int(input("Introduce un número: "))
# print(generarPares(numeroIntroducido))


# Ahora generador.

def generarPares(limite):

    numero = 1

    while numero < limite:
        yield numero*2
        numero += 1


numeroIntroducido = int(input("Introduce un número: "))
# Este es el objeto iterable que devuelve el generador.
sucesionPares = generarPares(numeroIntroducido)

# yield genera un objeto iterable, por lo que podemos recorrerlo con un for.
# for i in sucesionPares:
#  print(i)

# PERO en vez de recorrerlo con un for, podemos recorrerlo con next().
print(next(sucesionPares))
print("Ahora va el siguiente valor.")
print(next(sucesionPares))
# El programa nos va dando un valor cada vez que llamamos a next().
