def hay_repetidos(f):
    def wrapped(*args, **kwargs):
        resultado = f(*args, **kwargs)
        