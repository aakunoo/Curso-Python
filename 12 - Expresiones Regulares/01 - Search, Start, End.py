import re  # Importamos el módulo de expresiones regulares

cadena = "Estoy aprendiendo python todos los dias de la semana y en navidades."
busqueda = "navidades"

if re.search(busqueda, cadena) is not None:
    print("He encontrado el termino", busqueda)

else:
    print("No he encontrado el termino", busqueda)


# Start - End
# Nos permite saber la posición de inicio y fin de la cadena que estamos buscando

texto = "Viendo como funcionan las funciones de start y end, y tal vez span, tengo que repasar las tuplas, diccionarios y listas para manejar bien todo, sobretodo las listas."
busqueda2 = "listas"

texto_encontrado = re.search(busqueda2, texto)
# Con esto sabemos la posición de inicio del texto
print(texto_encontrado.start())
print(texto_encontrado.end())
# Nos devuelve una tupla con el inicio y fin del texto
print(texto_encontrado.span())

# Si hay mas de una repetición de la palabra, solo nos devolverá una, por eso debemos usar findall
# con len nos devuelve cuantas veces se repite la palabra
print(len(re.findall(busqueda2, texto)))
