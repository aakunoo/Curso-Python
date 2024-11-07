'''Para aprender el uso del condicional if vamos a crear un programa basico que 
evalue si un alumno ha aprobado o suspendido en base a la nota que ha obtenido.'''


def evaluar_alumno(nota):
    valoracion = "Desconocida"
    if nota < 5:
        valoracion = "Suspenso"
    # Si aqui pusieramos un if, el programa no funcionaria correctamente, ya que el else se ejecutaria siempre.
    elif nota > 10:
        valoracion = "Nota incorrecta"
    else:
        valoracion = "Aprobado"
    return valoracion


# con int() convertimos el valor introducido por el usuario a un entero
# input es para introducir un valor por consola.
notaAlumno = int(input("Introduce la nota del alumno: "))
print(evaluar_alumno(notaAlumno))
