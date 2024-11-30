class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getInfo(self):
        return "Nombre: " + self.nombre + ", Apellido: " + self.apellido + ", Edad: " + str(self.edad)

    def hablar(self):
        return "La persona " + self.nombre + " está hablando."

    def pensar(self):
        return "La persona " + self.nombre + " está pensando."

    def caminar(self):
        return "La persona " + self.nombre + " está caminando."

    def comer(self):
        return "La persona " + self.nombre + " está comiendo."


class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):
        # super().__init__(nombre, apellido, edad)
        Persona.__init__(self, nombre, apellido, edad)

        self.escuela = escuela

    def getInfo(self):
        return super().getInfo() + ", Escuela: " + self.escuela

    def estudiar(self):
        return "El estudiante " + self.nombre + " está estudiando."


class Trabajador(Persona):

    def __init__(self, nombre, apellido, edad, empresa):
        # super().__init__(nombre, apellido, edad)
        Persona.__init__(self, nombre, apellido, edad)

        self.empresa = empresa

    def getInfo(self):
        return super().getInfo() + ", Empresa: " + self.empresa

    def trabaja(self):
        return "El trabajador " + self.nombre + " está trabajando."


''' ---------------- Trabajando con herencia multiple. ---------------- '''


# El orden de las clases IMPORTA. La clase de mas a la izquierda tiene preferencia.
class Director(Trabajador, Estudiante):
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        # super().__init__(nombre, apellido, edad, empresa)
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        # super().__init__(nombre, apellido, edad, escuela)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.bonus = bonus

    def getInfo(self):
        return super().getInfo() + ", Bonus: " + str(self.bonus)

    def dirige(self):
        return "El director " + self.nombre + " esta dirigiendo."


persona1 = Persona("Laura", "Lopez", 20)

estudiante1 = Estudiante("Jero", "Vicente", 21, "IES Venancio Blanco")

print(persona1.getInfo())
print(estudiante1.getInfo())
print("----------------------")

trabajador1 = Trabajador("Carlos", "Romero", 49, "M3TECH")
print(trabajador1.getInfo())

director1 = Director("Pepe", "Lopin", 78, "AIR", "IES Venancio Blanco", 200)
print(director1.getInfo())

''' Para que la herencia multiple funcione correctamente,
NO se llama al super(), se llama a la clase directamente.
Ademas, tambien hay que poner self a la hora de llamar a los metodos de las clases padres.
Y se hace asi con todas las clases con las que se quiera trabajar.
'''
