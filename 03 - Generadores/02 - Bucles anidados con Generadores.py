# Con el * decimos que va a recibir un número indeterminado de parámetros y ademas lo tomara como tupla.
def capitales_mundo(*ciudades):
    for capital in ciudades:  # Accede al primer elemento de la tupla.
        for letracapital in capital:  # Se mete a buscar dentro de ese primer elemento.
            yield letracapital


# Como yield siempre devuelve un objeto iterable, creamos un objeto iterable.
# Estos parametros (aunque no los vemos) estan dentro de una tupla.
capitales_devueltas = capitales_mundo(
    "Bogotá", "México", "Buenos Aires", "Madrid", "París")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))

# Este programa nos imprime letra a letra, porque los subelementos de un elemento por ejemplo "Bogotá" son letras.

# PARA AHORRARNOS EL BUCLE ANINADO, PODEMOS USAR YIELD FROM:


def capitales_mundo(*ciudades):
    for capital in ciudades:
        # yield from desempaqueta la tupla y nos devuelve cada uno de los elementos.
        yield from capital


capitales_devueltas = capitales_mundo("Berlin", "Roma", "Londres", "Tokio")

print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))
