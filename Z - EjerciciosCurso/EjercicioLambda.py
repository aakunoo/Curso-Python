frase1 = "Los lunes son los mejores días para programar"
frase2 = "Python es moderno"
frase3 = "Veremos Inteligencia Artificial más adelante"
frase4 = "Lambda simplifica el código"

lista = [frase1, frase2, frase3, frase4]

lista.sort(key=lambda f: len(f), reverse=True)
print(lista)