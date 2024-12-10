import psycopg2

try:
    # Conexión a la base de datos
    conexion = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
    print("Conexión establecida con la BBDD.")
    cursor = conexion.cursor()

    query = """SELECT film_id, title, length
               FROM film
               WHERE title LIKE 'A%';"""

    cursor.execute(query)
    print("Datos obtenidos.")

    # Obtenemos los primeros 5 registros
    resultado = cursor.fetchmany(5)

    # Creamos el diccionario con la clave film_id y valor (title, length)
    dicc = {}
    for film_id, title, length in resultado:
        dicc[film_id] = (title, length)

    # Ahora generamos la lista de tuplas (film_id, length) con un bucle aparte
    lista = []
    for fid, valor in dicc.items():
        # valor es (title, length), así que valor[1] es length
        lista.append((fid, valor[1]))

    # Escribimos la información en el fichero
    # Formato requerido: film_id <<>> length
    with open("peliculas_info.txt", "w") as f:
        for film_id, length in lista:
            f.write(f"{film_id} <<>> {length}\n")

except psycopg2.OperationalError as e:
    print(f"Error de conexión a la base de datos: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
    print("Conexión cerrada.")
