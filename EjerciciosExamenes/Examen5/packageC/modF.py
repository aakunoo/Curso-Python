lista_cadenas = []


def recoger_datos():

    contadorA = 0
    contadorNoA = 0

    while True:
        cadena = input("Introduce una cadena (No escribas nada para terminar): ")
        if cadena == "":
            break

        if cadena != "":
            lista_cadenas.append(cadena)

            if "a" in cadena:
                contadorA += 1
                continue
            elif not "a" in cadena:
                contadorNoA += 1
                continue

    return (contadorA, contadorNoA)

#print(recoger_datos())

unir_con_coma = lambda a,b,c: f"{a},{b},{c}"
invertir_lista = lambda: lista_cadenas[::-1]

