
class Mayor(Exception):
    pass

def visualiza(num1 = 10, /, *, num2):
    try:
        match num1, num2:
            case int(), int():

                if num1 > num2:
                    raise Mayor("El primer número es mayor que el segundo.")
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                resultado = float(num1 / num2)
                print(f"El resultado de la división es: {resultado:08.3f}")

            case str(), str():
                cadena = str(num1+num2).upper()
                print(f"La concatenación de las cadenas es: {cadena:>30}")

            case _:
                print("Error: Los argumentos deben ser enteros o cadenas.")

    except Mayor as m:
        print(f"Error: {m}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        print("La función acaba aquí.")


visualiza(45, num2=30)
visualiza("Hola", num2="Adios")
visualiza(num2=15)