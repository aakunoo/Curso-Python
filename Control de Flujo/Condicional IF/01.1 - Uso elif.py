'''Viendo mas ejemplos del uso de elif.'''

# Si en este ejemplo, usaramos if en vez de elif el programa no funcionaria correctamente, ya que que leeria todas las condiciones.
print("Verificación de acceso")

notaAlumnov2 = int(input("Introduce tu nota: "))

if notaAlumnov2 < 5:
    print("Insuficiente")

elif notaAlumnov2 < 6:
    print("Suficiente")

elif notaAlumnov2 < 7:
    print("Bien")

elif notaAlumnov2 < 9:
    print("Notable")

else:
    print("Sobresaliente")
