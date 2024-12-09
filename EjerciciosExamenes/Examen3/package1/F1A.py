def nombres():
    contadorA = 0
    contadornoA = 0
    while True:
        nombre = input("Ingrese un nombre: ").strip()
        if not nombre == "":
            if nombre.__contains__("a"):
                contadorA += 1
                continue
            elif not nombre.__contains__("a"):
                contadornoA += 1
                continue
        else:
            lista = [contadorA, contadornoA]
            return lista

print(nombres())
juntar = lambda txt1, txt2, txt3: f"{txt3+txt2+txt1}"
