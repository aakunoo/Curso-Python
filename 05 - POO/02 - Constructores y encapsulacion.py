class Persona:
    __nombre = ""  # __ sirve para encapsular, es decir, que no se pueda modificar desde fuera de la clase
    apellido = ""
    edad = 0
    genero = "Sin definir"

    def __init__(self, nombre, apellido, edad, genero):  # Constructor (__init__)
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def hablar(self):
        return "La persona " + self.__nombre + " está hablando"

    def caminar(self):
        return "La persona " + self.__nombre + " está caminando"

    def getDatos(self):
        return "Nombre: " + self.__nombre + ", Apellido: " + self.apellido + \
            ", Edad: " + str(self.edad) + ", Genero: " + self.genero


p1 = Persona("Laura", "Lopez", 20, "Femenino")  # p1 es como self.
print(p1.getDatos())
p1.nombre = "zurron"  # No se puede modificar porque es privado
print(p1.getDatos())

p2 = Persona("Jero", "Vicente", 21, "Masculino")
print(p2.getDatos())
