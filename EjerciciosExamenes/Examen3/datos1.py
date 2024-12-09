import psycopg2

conexion = psycopg2.connect(dbname="dvdrental", user="postgres", password="")
try:
    print("Conexion establecida con la BBDD.")
    cursor = conexion.cursor()

    query = """SELECT film_id, description 
    FROM film 
    WHERE title LIKE '%a';"""

    cursor.execute(query)
    resultados = cursor.fetchmany(4) # Obtener los primeros 4 registros

    dicc = {}
    for result in resultados:
        dicc[result[0]] = result[1]  #film_id como clave, description como valor

    lista_tuplas = [(film_id, descripcion) for film_id, descripcion in dicc.items()]

    with open("peliculas.txt", "w") as archivo:
        for film_id, descripcion in lista_tuplas:
            archivo.write(f"{film_id} >> {descripcion}\n")
    print("Información guardada en 'peliculas.txt' con éxito.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar conexión a la base de datos
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
    print("Conexión cerrada.")