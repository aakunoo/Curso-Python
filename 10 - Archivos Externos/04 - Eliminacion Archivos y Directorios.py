import os
import io
''' Creamos el directorio con sus ficheros

os.makedirs("PruebaDirectorio")
os.chdir("PruebaDirectorio")

arch = open("Ejemplo.txt", "w")
arch2 = open("Ejemplo.docx", "w")

arch.write("Este es un fichero de prueba")
arch2.write("Archivo word de prueba")

print(os.getcwd())
print(os.listdir("./"))
'''

''' #Vamos a proceder a renombrar un archivo en concreto

os.chdir("PruebaDirectorio")

# Para renombrar archivos se usa .rename y hay que pasarle por parametros el nombre actual del fichero y el nuevo.
os.rename("Ejemplo.txt", "EjemploRenombrado.txt")
print(os.getcwd())
'''

# Para eliminar un archivo:

# os.chdir("PruebaDirectorio")

# os.remove("EjemploRenombrado.txt")
# print(os.listdir("./"))

# Para eliminar directorios:

os.chdir("PruebaDirectorio")
os.remove("Ejemplo.docx")
os.chdir("../")
os.rmdir("PruebaDirectorio")
print(os.listdir("./"))
