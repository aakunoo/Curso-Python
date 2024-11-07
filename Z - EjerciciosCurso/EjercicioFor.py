'''Crea una función que reciba dos listas por parámetros. La función debe comparar ambas listas,
devolviendo True si las listas son idénticas y False si no lo son'''


def compararListas(lista1, lista2):

    if (len(lista1)) != (len(lista2)):
        return False

    else:

        for i in range(0, len(lista1)):
            lista1[i] != lista2[i]
            return False
        return True


deportistas1 = ["Lebron", "Curry", "Bird"]
deportistas2 = ["Carslen", "Belmonte", "Gasol"]
print(compararListas(deportistas1, deportistas2))
