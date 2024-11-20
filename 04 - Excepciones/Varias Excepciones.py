def divide():

    try:
        op1 = (float(input("Introduce el primer número: ")))

        op2 = (float(input("Introduce el segundo número: ")))

        print("La división es: " + str(op1/op2))
    except ValueError |  ZeroDivisionError:
        print("El valor introducido es erróneo")


divide()
print("Calculo finalizado. Continuamos con el programa")
