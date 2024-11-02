''' Trabajo con Funciones. Sintaxis '''


def imprime_mensajes():  # Definicion (creacion) de la funcion.
    print("Estoy aprendiendo Python")
    print("De momento me esta gustando")
    print("Seguire aprendiendo")
    print("Hasta que me canse")


# Llamamos a la función.
imprime_mensajes()

print("El programa ha terminado su ejecución")

# Funcion en vez de con print, que nos devuelva un valor.


def funcion():
    # Solo se puede devolver un return por funcion.
    return "Este es el mensaje de la funcion"

# Con print(funcion()) nos imprime el valor en la consola.
# print(funcion())


# Esto me permite almacenar en una variable el valor que devuelve la funcion.
valorFuncion = funcion()
print(valorFuncion)

# ---------------------------- Funcion con parametros | argumentos ----------------------------

# Un parametro o argumento es una VARIABLE que se puede utilizar dentro de la funcion.

# Una funcion puede recibir n cantidad de parametros (los que sean necesarios e incluso de distinto tipo).


def imprimeMensajePersnalizado(mensaje, valor1, valor2):
    # Usamos str para convertir los valores a string y poder concatenarlos , porque los valores que se pasan por parametros tienen que ser del mismo tipo.
    return mensaje + str((valor1 + valor2))


print(imprimeMensajePersnalizado("La suma es = ", 5, 6))
