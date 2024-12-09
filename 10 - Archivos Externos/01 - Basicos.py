from io import open

# Vamos a realizar primero una creacion de un archivo y a continuacion vamos a escribir en el.
arch = open("primerArchivo.txt", "w")

# Para escribir en el archivo utilizamos el metodo write()
arch.write("Hola, este es mi primer archivo creado desde Python,\n Si hago esto se genera otra linea?\n AAAAA")

arch.close()

# Agregar mas texto al archivo
arch = open("primerArchivo.txt", "a")

# arch.write("\nEstoy agregando texto con open('archivo.txt', 'a')")
arch.close()

# Leer el archivo

arch = open("primerArchivo.txt", "r")

# Creamos una variable que almacene el contenido del archivo
contenido = arch.read()

arch.close()

print(contenido)

# En el caso de que el archivo sea muy grande, podemos leerlo linea por linea e incluso buscar una linea en especifico

arch = open("primerArchivo.txt", "r")
# readlines() nos devuelve una lista con todas las lineas del archivo
# readLine() nos devuelve la linea en la que se encuentra el puntero
contenidoLineas = arch.readlines()

arch.close()
print(contenidoLineas[3])
