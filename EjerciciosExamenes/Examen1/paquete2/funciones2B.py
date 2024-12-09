def ceros(f):
    def funcionInterna(*args, **kwargs):
        resultado = f(*args, **kwargs)
        conteo_ceros = str(resultado).count("0")
        print(f"Hay un total de {conteo_ceros} '0's")
        return resultado
    return funcionInterna

@ceros
def limpiar(cadena):
    return cadena.lstrip("0")

