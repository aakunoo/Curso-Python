'''
Ejercicio excepciones. Agregar elemento en una lista
• Crea un programa que pida introducir por consola 10 nombres propios de personas.
• Los nombres se guardarán en una lista.
• Si introducimos un nombre repetido, el programa lanzará una excepción de tipo
ValueError, la excepción nos informará del error con el texto “Error. Este nombre ya se
ha introducido”, y no se guardará el nombre repetido en la lista.
• Imprimir el contenido de la lista por consola.
'''

nombresPropios = []


def introducirNombres():
    for nombre in range(10):
        nombre = input("Introduce un nombre propio: ")
        if nombre in nombresPropios:
            raise ValueError("Error. Este nombre ya se ha introducido")
        nombresPropios.append(nombre)


try:
    introducirNombres()
    print(nombresPropios)
except ValueError as e:
    print(e)
