with open ("empleados.txt", "r") as fichero:
    lista = []
    for linea in fichero:
        id, nombre, apellido, salario = linea.strip().split(":")
        salario = int(salario)
        lista.append((id, nombre, apellido, salario))

for id, nombre, apellido, salario in lista:
    print(f"ID: {int(id):04d}, Nombre: {(nombre):^10}, Apellido: {(apellido):^10}, Salario: {float(salario):0.2f}")