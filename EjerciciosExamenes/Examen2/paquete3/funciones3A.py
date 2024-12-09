def calcula_promedio(*lista):
    return sum(*lista)/2

triplica = lambda num: 3*num
filtro_pares = lambda *lista2: [num for num in lista2 if num %2 == 0]
    