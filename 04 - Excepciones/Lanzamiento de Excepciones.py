import math

def calcularRaizCuadrada(numero):
    if numero < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(numero)
    
numeroUsusario = (int(input("Introduce un número: ")))

try:
    print(calcularRaizCuadrada(numeroUsusario))
except ValueError: 
    print("Número introducido es negativo, no se puede calcular la raíz cuadrada")
    
print("Y por aqui continua el programa...")