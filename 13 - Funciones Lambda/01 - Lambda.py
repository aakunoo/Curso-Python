''' Calcular area de un triangulo 
Con funciones normales y con funcion lambda. '''


'''def area_triangulo(base, altura):
    return (base * altura) / 2


triangulo1 = area_triangulo(5, 7)
triangulo2 = area_triangulo(15, 20)
print(triangulo1)
print(triangulo2)'''

# Con funcion lambda

# variable para almacenar la funcion lambda = lambda parametros: operacion que devuelve
area_triangulo = lambda base, altura: (base * altura) / 2

print(area_triangulo(5, 7))
print(area_triangulo(15, 20))

potencia = lambda base, exponente: base ** exponente
print(potencia(2, 4))

# Funcion lambda que le de formato a un valor numerico
comision_formato = lambda comision: "¡{}!€".format(comision)

comision_jero = 1500
print(comision_formato(comision_jero))

# Otro ejemplo

lista = [(100, 2), (20, 4), (30, 1), (15, 19), (8, 4)]
# Queremos ordenar la lista por la suma de los elementos de cada tupla

# Con funcion normal
'''
def ordena_lista(t):
    return t[0] + t[1]

# Basicamente es como decir: Ordename esta lista pero como te lo pido en la funcion ordena_lista.
lista.sort(key=ordena_lista)
print(lista)'''

# Con funcion lambda
lista.sort(key=lambda t: t[0] + t[1])
print(lista)
# key lo que hace es que le pasamos una funcion que se va a encargar de ordenar la lista

# Ahora vamos a trabajar con valores de texto
musicos = ["Paul McCartney", "John Lennon", "Ringo Starr", "George Harrison", "Tina Turner", "David Bowie", "Freddie Mercury"]
# Vamos a ordenar esta lista de musicos por apellido.

# Con funcion normal
'''def ordena_musicos(m):
    #Con split() separamos el nombre y el apellido de cada musico, y con el 1 le decimos que nos devuelva el apellido
    return m.split()[1]

musicos.sort(key=ordena_musicos)
print(musicos)'''

musicos.sort(key=lambda m: m.split()[1])
print(musicos)