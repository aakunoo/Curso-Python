from paquete2.funciones2A import producto, doble
import paquete2.funciones2B as f2b

def cuantos(num1, /, *, num2 = 5):    
    try:
        assert num2 <= 5
        
        match num1:
            case (a,b,c,d):
                return (a+b+c+d)
            case (a,b,c):
                if c == 0:
                    raise ZeroDivisionError("No se puede dividir entre 0.")
                return (a*b)/c
            case(a,b):
                if a == 0 or b == 0:
                    raise ZeroDivisionError("No se puede dividir entre 0.")
                return (a/b)
            case _:
                return "No se cumplen los parametros esperados."
                
    except AssertionError as ae:
        print(f"Error de aserción: {ae}")
    except ZeroDivisionError as zde:
        print(f"Error de división por cero: {zde}")
    except TypeError as te:
        print(f"Error de tipo de datos: {te}")
    except Exception as e:
        print(f"Error general: {e}")
    finally:
        print("Programa terminado")
        

print(cuantos((20,5)))
      
print(producto(5,6,3))
print(doble([10,20,30]))

f2b.limpiar("00001100101010")