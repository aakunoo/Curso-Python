def mayusculas(f):
    def funcionInterna(cadena):
        resultado = f(cadena)
        ponerMayus = str(resultado).upper()
        print(ponerMayus)
        return resultado
    return funcionInterna
        
@mayusculas
def mensaje(cadenaTexto):
    return f"Mensaje: {cadenaTexto}"
    
        
mensaje("quiero mucho A mi novia esto es una prueba.")