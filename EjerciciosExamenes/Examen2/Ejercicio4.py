def analiza_datos(num1, **kwargs):
    assert num1 > 0, "El número debe ser mayor que 0"
    
    try:
        for valor in kwargs.values():
            if valor == "Error":
                raise Exception("Se encontró un valor 'Error'")
            elif any(char.isdigit() for char in valor):
                continue
            else:
                print(valor.upper())
    except Exception as e:
        print(str(e))
    finally:
        print("El programa ha terminado")