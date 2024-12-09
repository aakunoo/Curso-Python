def mayor(num1, num2):
    """
    Calculates and prints the greater of two numbers.

    Parametross:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    None
    """
    print(f"El mayor de los numeros entre {num1} y {num2} es {max(num1, num2)}.")

mayor(6, 90)
mayor(num2=45, num1=89)

def area (altura, base = 8):
    """
    Calcula el área de un triángulo dado su altura y base.

    Parámetros:
    altura (float): La altura del triángulo.
    base (float, opcional): La base del triángulo. Por defecto es 8.

    Retorna:
    float: El área del triángulo.

    Ejemplo:
    >>> area(5, 10)
    25.0
    """
    return (base*altura)/2

print(area(7, 3))
print(area(altura=5))

def suma(*args):
    return sum(*args)

valores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(suma(valores))
    
def peque (**diccionario):
    return min(diccionario, key=diccionario.get)

habitaciones = {"salon":20, "cocina":15, "vestibulo": 7, "bagno": 9, "dormitorio": 18}
print(peque(**habitaciones))

def repetir (texto, /, *, entero):
    for _ in range(entero):
        print(texto)

repetir("repito", entero=6)

asignaturas = {"Interfaces":10, "AAD":8, "SGE": 5, "JAVA": 1, "Python": 3}
def funcion(f1, f2):
    print(f1)
    print(f2)
    
funcion(mayor(5, 8), peque(**asignaturas))

help(area)
help(mayor)