import re

lista_nombres = ["Jeronimo Vicente", "Laura Lopez",
                 "Alejandro Zurron", "Sara Garcia", "Javier Lopez", "Javier Vicente"]

# Queremos buscar los nombres que comiencen por "Javier"
for nombre in lista_nombres:
    if re.findall("^Javier", nombre):  # Si encuentra el nombre que comienza por "Javier"
        print(nombre)

for otroNombre in lista_nombres:
    if re.findall("Vicente$", otroNombre):  # Si encuentra el nombre que termina por "Lopez"
        print(otroNombre)

''' Metacaracter de []'''

lista_terminos = ["camión", "camion",
                  "automóvil", "automovil", "moto", "bicicleta"]
for termino in lista_terminos:
    # Si encuentra el termino que contenga "camión" o "camion"
    if re.findall("cami[oó]n", termino):
        print(termino)


''' Busqueda por rango de letras '''
print("---------------------")
for i in lista_terminos:
    # Nos imprime todos los terminos dentro de esta lista que contengan alguna letra entre la p y la z.
    if re.findall("[p-z]", i):
        print(i)

''' Encontrar todos aquellos terminos cuya primera letra este entre a y f. '''
print("---------------------")
for j in lista_terminos:
    if re.findall("^[a-f]", j):
        print(j)

# Las busquedas distinguen entre mayusculas y minusculas.

''' Encontrar todos los terminos que terminen por x caracteres '''
print("---------------------")
for h in lista_terminos:
    if re.findall("[l-p]$", h):
        print(h)


''' Tenemos estos productos, y queremos hacer una busqueda que nos encuentre los codigos de Ma1,2 y 3. '''
print("---------------------")
lista_productos = ["Ma:1", "Se1", "Ma2", "Va.1", "Ba.1",
                   "Ma3", "Se2", "Ma.4", "Se3", "SeA", "SeB", "Va2", "SeC"]

for producto in lista_productos:
    # Asi decimos que nos busque todo lo que contenga Ma y ademas un numero entre el 1 y el 3.
    if re.findall("Ma[1-3]", producto):
        print(producto)

''' Si a esto ultimo le ponemos ^ de la siguiente forma:
if re.findall("Ma[^1-3]", producto):
es como decir que queremos que nos busque todos aquellos prodcutos que NO 
contengan un numero del 1 al 3 despues de Ma.
'''

''' Busqueda que nos encuentre tanto valores numericos como letras y ademas con rangos. '''

print("---------------------")
for producto2 in lista_productos:
    if re.findall("Se[0-2A-B]", producto2):
        print(producto2)

''' Busquedas de caracteres como = . : , - '''

print("---------------------")
for producto3 in lista_productos:
    if re.findall("Ma[.:]", producto3):
        print(producto3)
