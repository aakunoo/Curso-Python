class Vehiculo():
    num_vehiculos = 0

    def __init__(self, modelo, anio, color, propietario):
        self._nombreOculto = modelo
        self.anio = anio
        self.color = color
        self.propietario = propietario
        Vehiculo.num_vehiculos +=1

    @property
    def modelo(self):
        return self._nombreOculto

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._nombreOculto = nuevo_modelo

    def detalles(self):
        return (self.modelo, self.anio, self.color, self.propietario)


class Coche(Vehiculo):
    def __init__(self, modelo, anio, color, propietario, potencia, combustible):
        super().__init__(modelo, anio, color, propietario)
        self.potencia = potencia
        self.combustible = combustible

    def detalles(self):
        return super().detalles() + (self.potencia, self.combustible)

    def __gt__(self, other):
        if isinstance(other, Coche):
            return self.potencia > other.potencia
        return NotImplemented

Coche1 = Coche("Peugeot", 2000, "Rojo", "Jero", 4000, True)
Coche2 = Coche("Nissan", 2013, "Verde", "Jero", 6000, True)

print(Coche2.__gt__(Coche1))
