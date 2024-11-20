''' Codigo de Pildoras Informaticas. '''
import sys


def suma(num1, num2):
    return num1+num2


def resta(num1, num2):
    return num1-num2


def multiplica(num1, num2):
    return num1*num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación erronea"


intentos = 0

while True:  # While True es un bucle infinito.
    try:
        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))

        break  # Si no hay error, salimos del bucle.
    # Excepcion que se lanza cuando el valor introducido no es lo que se espera.
    except ValueError:
        intentos += 1
        print("El valor introducido es erróneo")
        if (intentos == 3):
            print("Demasiados intentos, el programa ha finalizado.")
            sys.exit()  # Sale del programa.


operacion = input(
    "Introduce la operación a realizar (suma,resta,multiplica,divide): ")
if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")
