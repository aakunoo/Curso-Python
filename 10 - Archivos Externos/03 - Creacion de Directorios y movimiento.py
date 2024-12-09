import os  # Importamos la librería os para poder trabajar con el sistema operativo
from io import open  # Importamos la librería open para poder trabajar con archivos

# os.mkdir("10.1 - Creando un directorio")  # Creamos un nuevo directorio

os.chdir("10.1 - Creando un directorio")  # Cambiamos de directorio

arch = open("ficheroEnNuevoDirectorio.txt", "w")
arch.write("Supuestamente estoy escribiendo en un fichero creado en el nuevo directorio\nNo lo se, lo verificare en breve\nAmo a mi novia.")


print(os.getcwd())  # Imprimimos el directorio actual
# Imprime todos los elementos a modo de lista, pudiendo realizar operaciones de todo tipo con listas.
print(os.listdir("./"))
