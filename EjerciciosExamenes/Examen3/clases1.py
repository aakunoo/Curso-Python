class perro():
    num_perros = 0

    def __init__(self, nombreOculto, edad, color, dueno):
        self.__nombreOculto = nombreOculto
        self.edad = edad
        self.color = color
        self.dueno = dueno
        perro.num_perros += 1

    # Getter para nombre
    @property
    def nombre(self):
        return self.__nombreOculto

    # Setter para nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombreOculto = nombre

    def datos(self):
        return (self.color, self.dueno)

Perro1 = perro("a", 20, "Rojo", True)

print(Perro1.datos())

class galgo(perro):

    def __init__(self, nombre, edad, color, dueno, velocidad, peso):
        super().__init__(nombre, edad, color, dueno)
        self.velocidad = velocidad
        self.peso = peso

    def datos(self):
        return super().datos() + (self.velocidad,)

    def __add__(self, other):
        if isinstance(other, galgo):
            return self.peso + other.peso
        return NotImplemented

Perro1 = perro("Max", 5, "Marrón", "Juan")
print(Perro1.datos())  # ('Marrón', 'Juan')

Galgo1 = galgo("Luna", 3, "Gris", "Carlos", 40, 15)
Galgo2 = galgo("Rocky", 4, "Negro", "Ana", 50, 20)

print(Galgo1.datos())  # ('Gris', 'Carlos', 40)
print(Galgo1 + Galgo2)  # 35 (15 + 20)

