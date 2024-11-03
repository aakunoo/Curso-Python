''' Otro ejemplo del condicional IF. Viendo los operadores logicos and y or. '''
# and = y además. (Hay que cumplir todas las condiciones que una el operador)
# or = o si no. (Hay que cumplir una de las condiciones que una el operador)

'''
print('Obtencion carnet de conducir')

edad = int(input('Introduce tu edad: '))
vision = input('Tienes buena vision? (si/no): ')

# Puede obtener el carnet si cumple todas las condiciones. (Edad entre 18 y 90 años y buena vision)
if edad >= 18 and edad <= 90 and vision == 'si':
    print('Tienes la edad requerida para poder sacarte el carnet de conducir.')

else:
    print("No cumples los requisitos.")
'''


# ---------------------------- Ejemplo con operador or ----------------------------

print("Obtencion de beca escolar")

nota_media = int(input("Introduce tu nota media: "))
hermanos_en_centro = int(
    input("Introduce el numero de hermanos en el centro: "))
distancia_centro = int(input("Introduce la distancia al centro en km: "))
renta_familiar = int(input("Introduce la renta familiar anual: "))

# Basicamente el ejercicio dice que la nota media de 8, O SI NO, tener mas de 3 hermanos en el centro,
# O SI NO, vivir a mas de 10 km del centro, O SI NO, tener una renta familiar inferior a 20000 euros.
# Con que se cumpla una condicion de todas ellas se obtiene la beca.

if nota_media > 8 or hermanos_en_centro > 3 or distancia_centro > 10 or renta_familiar < 20000:
    print("Tienes derecho a beca.")

else:
    print("No tienes derecho a beca.")
