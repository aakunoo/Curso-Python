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

for i in sucesionPares:
    print(i)
