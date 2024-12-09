import re

nombre1 = "Jeronimo Vicente"
nombre2 = "Laura Lopez"
nombre3 = "Alejandro Zurron"
nombre4 = "Jara Martin"
nombre5 = "Para Perez"
codigo1 = "frregergwefwq255grewggw"
codigo2 = "255fhbwebfnewbf"
codigo3 = "ewfege133brefhjebhf"

# Son dos parametros por default, pero podemos agregar un tercero que es el que nos permite ignorar las mayusculas.
if re.match("Jeronimo", nombre1, re.IGNORECASE):
    print("He encontrado el nombre")

else:
    print("No lo he encontrado")

# El . sirve para "ignorar" el primer caracter.
if re.match(".ara", nombre4, re.IGNORECASE):
    print("He encontrado el nombre")
else:
    print("No lo he encontrado")

# Search

if re.search("255", codigo2):
    print("He encontrado el codigo")
else:
    print("No lo he encontrado")
