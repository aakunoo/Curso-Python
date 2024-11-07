''' Las listas se escriben con corchetes y los elementos separados por comas. '''

trabajadores = ["Pedro", "Ramón", "Juan", 5]


# append nos permite agregar un nuevo elemento a la lista.
trabajadores.append("Pepe")

# len nos permite saber cuantos elementos tiene la lista.
print(len(trabajadores))

print(trabajadores)
# Imprime el elemento en la posición 4 de la lista.
print(trabajadores[4])

# Imprime el primer elemento de la lista empezando por atras.
print(trabajadores[-1])

# Imprime 3 elementos empezando desde la posicion 0.  El conteo de elementos (segundo digito) empieza SIEMPRE desde el principio.
print(trabajadores[0:3])

# extend permite añadir una lista a la lista inicial.
trabajadores.extend(["Jero", 9, True])
print(len(trabajadores))
print(trabajadores)

# insert añade un elemento en una posición o índice determinado. -> (nombrelista).insert(posición, (loquequieresagregar))
trabajadores.insert(0, "Elemento 0")
print(trabajadores)

# remove sirve para borrar lo que le indiques de la lista.
trabajadores.remove("Elemento 0")
print(trabajadores)

# pop() elimina parametros de la lista, si no se le indica nada, elimina el último elemento, si no, elimina el elemento que le indiques.
trabajadores.pop()
print(trabajadores)

# reverse invierte todos los parametros de la lista (no se le pasan parametros).
trabajadores.reverse()
print(trabajadores)

# sort ordena los elementos de la lista de menor a mayor.
# trabajadores.sort (Enteros)
# print(trabajadores)

# sort(reverse=True) ordena los elementos de la lista de mayor a menor.
# trabajadores.sort(reverse=True) (Solo con enteros)
# print(trabajadores)

# index nos permite saber en que posición se encuentra un elemento.
print(trabajadores.index("Jero"))

# para unir dos listas se usa el signo + .
trabajadores2 = ["Jero", "Zurron", "Laura"]
print(trabajadores + trabajadores2)

# del elimina un elemento de la lista indicando el índice.
del trabajadores[0]
print(trabajadores)

# count nos permite saber cuantas veces se repite un elemento en la lista.
print((trabajadores+trabajadores2).count("Jero"))
