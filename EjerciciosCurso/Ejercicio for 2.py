'''Crea un programa de Python que pida 2 números por consola. 
El programa debe imprimir todos los números primos comprendidos entre los 2 números introducidos por consola.'''

print("Calculadora de numeros primos!")
print("------------------------------")


numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))


def numerosPrimeros(numero):

    for j in range(2, numero):
        if numero % j == 0:
            return False
    print(str(numero) + " es primo")
    return True


for i in range(numero1, numero2):
    numerosPrimeros(i)
