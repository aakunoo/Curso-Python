''' Distintos ejemplos de conversiones de datos '''

# ------------------------------ Conversion de string a entero. ------------------------------
a = "15"
b = "35"
# Ponemos int(a)+int(b) porque las variables estan declaradas como strings y queremos pasarlas a enteros para poder sumarlas.
print(int(a)+int(b))

# ------------------------------ Conversion de String a Float. ------------------------------
c = "15.25"
b = "35.55"
# Ponemos float(c)+float(d) porque las variables estan declaradas como strings y queremos pasarlas a float para poder sumarlas.
print(float(c)+float(b))

# ------------------------------ Conversion de entero a String. ------------------------------
edad = 26
# Ponemos "Tengo " + str(edad) + " años" porque queremos concatenar la cadena de texto con la variable edad que es un entero.
print("Tengo " + str(edad) + " años")

# ------------------------------ Convertir una lista en texto. ------------------------------
empleados = ["Pedro", "Ramón", "Juan", "Laura", "Jero"]
# join necesita un separador para unir los elementos de la lista, podemos poner el que queramos, con la sintaxis: "separador".join(nombreLista)
print(" | ".join(empleados))

# ------------------------------ Convertir un String en una lista. ------------------------------
empleados2 = "Pedro, Ramón, Juan, Laura, Jero"
# split es para transformar un string en una lista.
print(empleados2.split())
