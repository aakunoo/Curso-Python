'''
A partir de este punto, vamos a crear un archivo csv, y vamos a leerlo con python.
Un fichero csv es un fichero normalmente exportado de una hoja de calculo, y que contiene datos separados por un separador.
CSV ficheros utilizados para almacenar una gran cantidad de datos, como los datos de un usuario en un sistema de autenticacion, o los datos de un producto en un sistema de inventario.
'''

import csv
with open('Equipos.csv', newline='') as csvfile:
    # En el delimiter se pone el separador que se uso en el archivo csv.
    # quotechar es el caracter que se uso para encerrar los datos.
    micsv = csv.reader(csvfile, delimiter=';', quotechar='|')
    for linea in micsv:
        print('-'.join(linea))
