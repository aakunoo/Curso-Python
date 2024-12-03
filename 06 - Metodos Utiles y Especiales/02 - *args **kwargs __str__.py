class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return "Datos de la persona: \n" + "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad)


p1 = Persona("Jero", "Vicente", 21)

print(p1)  # No hace falta poner un .__str__() porque ya lo hace por defecto.
print("--------------------------------------------------")


class Parametros():

    almacen_datos = []

    # * significa que puede recibir un numero indeterminado de parametros.
    # * es una tupla.
    def __init__(self, *datos):

        for dato in datos:
            self.almacen_datos.append(dato)

        self.getInfo(self.almacen_datos)

    # def __str__(self):
    #   return "Datos almacenados: " + str(self.almacen_datos)

    def getInfo(self, info):
        for dato in info:
            print(dato)


prueba1 = Parametros("Hola", 5, 10000, "Laura", "Curso")
# print(prueba1.__str__())
print("--------------------------------------------------")


class Person():

    # Cuando llamemos al metodo constructor, le pasaremos un diccionario con los datos.
    # ** es un diccionario.
    def __init__(self, **data):
        # Devuelve una lista de tuplas con los elementos del diccionario.
        elementos = data.items()

        for clave, valor in elementos:
            print(clave, ":", valor)


prueba2 = Person(Nombre="Jero", Apellido="Vicente", Edad=21)
