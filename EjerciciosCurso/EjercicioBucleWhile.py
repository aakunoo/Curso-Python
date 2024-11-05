'''
Ejercicio bucles y condicionales. Número aleatorio
Se trata de elaborar un programa que genere un número aleatorio entre 1 y 100. Para ello
debemos importar el módulo random y utilizar la instrucción random.randint(1,100). Esta
instrucción genera un número entero entre 1 y 100.
A continuación, se le pide al usuario que introduzca un número por consola entre 1 y 100. Si el
número introducido por el usuario es menor, se imprime en consola un mensaje indicando que
el número aleatorio es mayor que el introducido por él. Si el número introducido por el usuario
es mayor que el aleatorio, se imprime un mensaje indicando que el número aleatorio es menor
que el introducido por él. Después de indicar si es mayor o menor, se vuelve a pedir al usuario
que introduzca un número entre 1 y 100.
Se trata de averiguar cuál es el número aleatorio generado por el programa a base de ir
aproximándonos intento tras intento, y hacerlo en el menor número de intentos posibles así que
también debemos controlar cuántos intentos consume el usuario para adivinar el número
aleatorio generado por el programa.
Cuando el usuario averigüe finalmente el número aleatorio, el programa imprimirá en consola
“Correcto. Has utilizado…” y el nº de intentos consumidos
'''

import random

print("Juego de adivinar un numero random!")

numero = random.randint(1, 100)
contador = 1

numeroUsuario = int(input("Introduce un numero del 1 al 100!: "))

while numeroUsuario < 0 or numeroUsuario > 100:
    print("Debes introducir un numero del 1 al 100 para jugar!")
    numeroUsuario = int(input("Introduce un numero del 1 al 100!: "))
    contador = contador + 1

    while numeroUsuario > 0 and numeroUsuario <= 100:
        if numeroUsuario > numero:
            print("El numero que tienes que adivinar es menor!")
            numeroUsuario = int(input("Prueba suerte con otro numero!: "))
            contador = contador+1

        elif numeroUsuario < numero:
            print("El numero que tienes que adivinar es mayor!")
            numeroUsuario = int(input("Prueba suerte con otro numero!: "))
            contador = contador+1

        elif numeroUsuario == numero:
            print("Enhorabuena! Has acertado el numero en un total de " +
                  str(contador) + " intentos!")
            if contador >= 10:
                print(
                    "Has hecho demasiados intentos! Intentalo de nuevo a ver si mejoras! >:)")
            elif contador < 10:
                print("WOW! Felicidades! Menos de 10 intentos! Buena!")
            break
