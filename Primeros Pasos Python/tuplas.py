''' Las tuplas se escriben con paréntesis y los elementos separados por comas. 
    Conversion de tuplas a listas y viceversa. '''

mydata = ("Jeronimo", 26, 11, 2003)

# Para convertir una tupla en una lista se usa list((nombre de la tupla))
mydatalist = list(mydata)

mydatav2 = ["Laura", 1, 6, 2004]

# Para convertir una lista en una tupla se usa tuple((nombre de la lista))
mydatav2tupla = tuple(mydatav2)

# print(mydatalist)
# print(mydatav2tupla)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""Trabajo con tuplas (metodos)"""

misDatos = ("Jeronimo", 26, 11, 2003)

# Con esto sabemos si el entero 26,  esta dentro de nuestra tupla "misDatos". (True si lo esta, False si no lo esta)
print(26 in misDatos)

# Para saber cuantas veces se encuentra el parametro que indiquemos en la tupla en la que se usa count.
print(misDatos.count("Jeronimo"))

# Metodo len para saber cuantos elementos tiene la tupla.
print(len(misDatos))

# Metodo index para saber en que posición se encuentra un elemento.
print(misDatos.index("Jeronimo"))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' Desempaquetado de tuplas (consiste en asignar los valores de una tupla a variables) '''

datosLaura = ("Laura", 1, 6, 2004)
# Asi pasamos | nombre = Laura | dia = 1 | mes = 6 | agno = 2004 | convirtiendolo en variables.
nombre, dia, mes, agno = datosLaura
print(nombre)
print(agno)
