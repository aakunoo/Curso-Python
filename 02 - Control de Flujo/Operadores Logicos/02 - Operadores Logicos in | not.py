''' Trabajando con los operadores logicos not e in. '''


# ---------------------------- Operador in ----------------------------
trajadores = ['Juan', 'Ana', 'Luis', 'Pedro', 'Maria']

# Muchas veces va a surgir la necesidad de ver si un valor se encuentra o no en una lista.
if 'Juan' in trajadores:  # Si Juan se encuentra en la lista de trabajadores:
    print('Juan trabaja aqui.')
else:
    print('Juan no trabaja aqui.')

# Igual que hacemos busquedas en una lista podemos hacerlas en un string.

lenguajes_de_programacion = 'Python, Java, C++, C#, JavaScript'

if 'Python' in lenguajes_de_programacion:
    print('Python es un lenguaje de programacion.')
else:
    print('Python no es un lenguaje de programacion.')


# ---------------------------- Operador not ----------------------------

if "SQL" not in lenguajes_de_programacion:
    print("SQL no es un lenguaje de programacion.")
else:
    print("SQL es un lenguaje de programacion.")
