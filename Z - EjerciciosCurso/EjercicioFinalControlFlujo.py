diccionario1 = {}  # Declaramos un diccionario VACIO.

pais = input("Introduce un pais: ")  # Introducimos un pais.

while pais != "salir":  # Mientras PAIS se distinto de "salir":

    ciudad = input("Introduce una ciudad: ")  # Introducimos una ciudad.

    # setdefault() nos devuelve el valor del pais, si no existe lo crea.
    listaciudades = diccionario1.setdefault(pais, [ciudad])
    # Si SI existe la clave pais, entra en el IF
    # Si la lista de ciudades es distinta a la ciudad introducida:
    if listaciudades != [ciudad]:

        # ñadimos la ciudad junto con su clave a la lista de ciudades.
        diccionario1[pais].append(ciudad)

    # Volvemos a introducir un pais y empieza el bucle de nuevo,.
    pais = input("Introduce un pais: ")

print(diccionario1)
