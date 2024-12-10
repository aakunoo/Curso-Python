def existe_repetido(f):
    def wrapped(*args, **kwargs):
        resultado = f(*args, **kwargs)


        return resultado
    return wrapped
