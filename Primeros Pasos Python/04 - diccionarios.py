'''Trabajo con diccionarios
Vamos a trabajar con capitales del mundo (Almacenar capitales)'''

# Nombre del diccionario = {clave: valor}
lasCapitales = {"Spain": "Madrid", "France": "Paris",
                "Italy": "Rome", "Germany": "Berlin", "Portugal": "Lisbon"}

print(lasCapitales)

# Para anadir un nuevo elemento al diccionario. NombreDiccionario[clave] = valor
lasCapitales["Colombia"] = "Bogota"
print(lasCapitales)

# Para modificar el valor de una pareja clave:valor, ponemos la clave y le asignamos el nuevo valor. nombreDiccionario[clave] = nuevoValor
# lasCapitales["Spain"] = "Barcelona"
# print(lasCapitales)

# Eliminar elemento del diccionario. -> del nombreDiccionario[clave]
del lasCapitales["Colombia"]
print(lasCapitales)

# ------------------------------ Otro ejemplo ------------------------------

# Vamos a usar tuplas para asignar CLAVES.

claveCapitales = ("Spain", "France", "Italy", "Germany", "Portugal")

# Ahora creo un diccionario con las claves de la tupla y asigno los valores.
capitalesMundo = {claveCapitales[0]: "Madrid", claveCapitales[1]: "Paris",
                  claveCapitales[2]: "Rome", claveCapitales[3]: "Berlin", claveCapitales[4]: "Lisbon"}
print(capitalesMundo)

# Para acceder a un valor de un diccionario, se hace igual que con las listas y tuplas, poniendo el nombre del diccionario y entre corchetes la clave.
print(capitalesMundo["Spain"])

# keys se usa para saber todas las claves del diccionario.
print(capitalesMundo.keys())

# values se usa para saber todos los valores del diccionario.
print(capitalesMundo.values())

# len se usa para saber cuantos elementos tiene el diccionario. (Igual que con las listas y tuplas)
print(len(capitalesMundo))

# ------------------------------ Diccionarios anidados ------------------------------

datosJordan = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago Bulls",
               # Usamos una lista dentro del diccionario.
               "Anillos": (1991, 1992, 1993, 1996, 1997, 1998)}

print(datosJordan)
print(datosJordan["Anillos"])

# Para usar un diccionario dentro de otro diccionario:
datosCurry = {30: "Curry", "Nombre": "Stephen", "Equipo": "Golden State Warriors",
              "Anillos": {"Temporada": [2015, 2017, 2018]}}

print(datosCurry.keys())
print(datosCurry)
print(datosCurry["Anillos"])
print(datosCurry["Anillos"]["Temporada"])
