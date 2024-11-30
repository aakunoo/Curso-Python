class Persona:
    __nombre = ""  # __ sirve para encapsular, es decir, que no se pueda modificar desde fuera de la clase
    apellido = ""
    __edad = 0
    genero = "Sin definir"

    def __init__(self, nombre, apellido, genero):  # Constructor (__init__)
        self.__nombre = nombre
        self.apellido = apellido
        # self.edad = edad
        self.genero = genero

    # Como hacemos para introducir desde fuera de la clase un valor en edad? Usamos un setter.

    def setEdad(self, laEdad):
        if laEdad < 0 or laEdad > 100:
            print("Edad incorrecta")
        else:
            self.__edad = laEdad
            return self.__edad

    def hablar(self):
        return "La persona " + self.__nombre + " está hablando"

    def caminar(self):
        return "La persona " + self.__nombre + " está caminando"

    def getDatos(self):
        return "Nombre: " + self.__nombre + ", Apellido: " + self.apellido + \
            ", Edad: " + str(self.__edad) + ", Genero: " + self.genero


p1 = Persona("Laura", "Lopez", "Femenino")
p1.setEdad(30)

# p1 es como self.
print(p1.getDatos())
# p1.nombre = "zurron"  # No se puede modificar porque es privado
# print(p1.getDatos())

p2 = Persona("Jero", "Vicente", "Masculino")
p2.setEdad(49)
print(p2.getDatos())


# Metodos de acceso.
# Setters: Permiten establecer el valor de un atributo.
# Getters: Acceder al valor almacenado en un atributo.
