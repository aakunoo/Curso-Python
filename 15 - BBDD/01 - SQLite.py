import sqlite3

conexion = sqlite3.connect("15 - BBDD/BBDDSQLiteCasa")

puntero = conexion.cursor()
#puntero.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#puntero.execute("INSERT INTO PRODUCTOS VALUES('Camiseta', 25, 'Moda')")

'''productos = [
    ("Patin",100, "Deportes"),
    ("Cenicero",20, "Ceramica"),
    ("Pantalon",60, "Moda")
]

puntero.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", productos)'''

puntero.execute("SELECT * FROM PRODUCTOS")
productos = puntero.fetchall() # Convierte los registros que la instruccion sql devuelve en una lista.

for p in productos:
    print(f"Nombre: {p[0]}, Precio: {p[1]}")



puntero.close()
conexion.close()