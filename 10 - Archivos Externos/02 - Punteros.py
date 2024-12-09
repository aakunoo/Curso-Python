from io import open

# Doble lectura
arch1 = open("primerArchivo.txt", "r")

print(arch1.read())

arch1.seek(6)  # Esto mueve el puntero al inicio del archivo

print(arch1.read())

# Sale vacio ya que el puntero se encuentra al final del archivo
# seek() nos permite mover el puntero a una posicion especifica

# seek lee desde el caracter que indiquemos en adelante
# si ponemos sin embargo un valor en arch1.read(6) nos leera SOLO los primeros 6 caracteres
