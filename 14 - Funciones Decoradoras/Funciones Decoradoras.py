def funcionDecoradora(f):
    
    def funcionInterna():
        print("A continuacion vamos a realizar un calculo.")
        f()
        print("Ya he terminado el calculo")
    return funcionInterna

@funcionDecoradora
def suma ():
    print(25+30)
  

def resta():
    print(80-25)

suma()
resta()