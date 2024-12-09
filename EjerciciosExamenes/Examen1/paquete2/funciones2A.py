def verdad(*args):
    valores_true = (args).count(True)
    valores_false = (args).count(False)
    return [valores_false, valores_true]

print(verdad(False, True, True))

producto = lambda num1, num2, num3: (num1*num2*num3)
doble = lambda lista: lista + lista
