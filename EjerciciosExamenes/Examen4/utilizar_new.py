class LimiteExcedido(Exception):
    pass

def procesar(param1, /, *, param2 = 5):
    try:
        assert param2 <= 5, "El segundo parametro debe ser menor que 5"
        match param1:
            case (a,b,c,d):
                return (a+b+c+d)

            case (a,b,c):
                if c == 0:
                    raise ZeroDivisionError ("No se puede dividir por 0.")
                return (a*b)/c

            case(a,b):
                resultado = a/b
                if b == 0:
                    raise ZeroDivisionError("No se puede dividir por 0.")
                if resultado > 100:
                    raise LimiteExcedido("Has superado el limite. ")
                return resultado
            case _:
                print("Parametros no validos.")


    except LimiteExcedido as lm:
        print(f"Error: {lm}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"Error general: {e}")
    else:
        print("No ocurrieron excepciones")
    finally:
        print("Proceso finalizado")

procesar((2,2))
procesar((3,6,0), param2=5)
procesar((10,20,30,40), param2=4)


