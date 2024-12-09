from io import open
'''
Hola, este es mi primer archivo creado desde Python,
Si hago esto se genera otra linea?
AAAAA
Estoy agregando texto con open('archivo.txt', 'a')
'''
nuevaLinea = "Estoy realizando un ejercicio de sustitucion de linea"

with open("primerArchivo.txt", "r+") as arch:
    lines = arch.readlines()
    lines[2] = nuevaLinea + "\n"
    arch.seek(0)
    arch.writelines(lines)
