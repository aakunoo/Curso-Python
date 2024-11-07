Capitales = {"Spain": "Madrid", "France": "Paris", "Indonesia": "Jakarta",
             "Italy": "Rome", "Germany": "Berlin", "Portugal": "Lisbon"}

for i in Capitales:
    valor = Capitales[i]
    print(i)
    print(valor)


# Items imprime las claves y los valores del diccionario.
print(Capitales.items())

# Imprime las claves y los valores del diccionario.
for clave, valor in Capitales.items():
    print(clave + " -> " + valor)
