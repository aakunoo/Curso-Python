import psycopg2

with open("registros.txt", "r") as fichero:
    lista = []
    for registro in fichero:
        numero, nombre, apellido = registro.strip().split(":")
        numero = int(numero)
        lista.append((numero, nombre, apellido))

for numero, nombre, apellido in lista:
    numero = f"{float(numero):06.2f}"
    nombre = f"{(nombre):^10s}"
    
    print (f"Numero: {numero}, Nombre: {nombre}, Apellido: {apellido}")
    
conexion = psycopg2.connect(
    database="dvdrental",
    user="jero",
    password="261103",
    host="localhost",
    port="5432"
)

puntero = conexion.cursor()

for numero, nombre, apellido in lista:
    query = """
        INSERT INTO actor (actor_id, first_name, last_name)
        VALUES (%s, %s, %s)
    """
    puntero.execute(query, (numero, nombre, apellido))

conexion.commit()
print("Registros añadidos correctamente en la tabla 'actor'.")

puntero.close()
conexion.close()
print("Conexión con la base de datos cerrada.")