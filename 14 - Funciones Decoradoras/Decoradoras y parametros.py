def funcionDecoradora(f):
    
    def funcionInterna(*args, **kwargs):
        print("A continuacion vamos a realizar un calculo.")
        f(*args, **kwargs)
        print("Ya he terminado el calculo")
    return funcionInterna

@funcionDecoradora
def suma(numero1, numero2):
    print(numero1 + numero2)
  

def resta(numero1, numero2):
    print(numero1 - numero2)


@funcionDecoradora
def potencia(base, exponente):
    print(pow(base, exponente))


suma(5,7)
resta(7,5)
potencia(base=5,exponente=3)