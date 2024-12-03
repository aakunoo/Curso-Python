'''
Creamos en el directorio de nuestro proyecto un archivo llamado setup.py
En este archivo vamos a escribir las popiedades o informacion que queremos que tenga nuestro paquete.

from setuptools import setup

setup(
    name="calculosbasicosmatematicos",
    version="1.0",
    description="Paquete para calculos basicos, suma, resta y multiplicacion",
    author="Jeronimo",
    author_mail="contact@jeronimovicente.com",
    url="",
    packages=["Paquetes", "Paquetes.CalculosBasicos"]
)


Luego en la terminal, escribimos:

❯ python setup.py sdist


Una vez que se haya creado el archivo .tar.gz, vamos a la terminal y escribimos:
pip3 install nombre_del_paquete.tar.gz

Y asi lo podriamos usar como usamos cualquier otro modulo de python. (Math, random, etc)
'''
