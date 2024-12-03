class Vehiculo():

    def __init__(self, color, ruedas, ancho, alto, asientos, marchas):
        self.color = color
        self.ruedas = ruedas
        self.ancho = ancho
        self.alto = alto
        self.asientos = asientos
        self.marchas = marchas
        self.acelerando = False
        self.frenando = False
        self.girando = False
        self.atras = False

    def acelerar(self):
        self.acelerando = True

    def frenar(self):
        self.frenando = True

    def girar(self):
        self.girando = True

    def marchaAtras(self):
        self.atras = True

    def getInfo(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Ancho: {self.ancho}, Alto: {self.alto}, Asientos: {self.asientos}, Marchas: {self.marchas} "


class Bicicleta (Vehiculo):
    def __init__(self, color, ruedas, ancho, alto, asientos, marchas):
        super().__init__(color, ruedas, ancho, alto, asientos, marchas)
        self.saltando = False

    def getInfo(self):
        return super().getInfo()

    def saltar(self):
        self.saltando = True


class Coche (Vehiculo):
    def __init__(self, color, ruedas, ancho, alto, asientos, marchas, aire, carga, cilindrada):
        super().__init__(color, ruedas, ancho, alto, asientos, marchas)
        self.aire = aire
        self.carga = carga
        self.cilindrada = cilindrada

        self.arrancando = False
        self.cargando = False
        self.derrapando = False

    def getInfo(self):
        return super().getInfo() + f", Aire acondicionado: {self.aire}, Carga (kg): {
            self.carga}, Cilindrada: {self.cilindrada} "

    def arrancar(self):
        self.arrancando = True

    def cargar(self):
        self.cargando = True

    def derrapar(self):
        self.derrapando = True


class Furgoneta(Coche):
    def __init__(self, color, ruedas, ancho, alto, asientos, marchas, aire, carga, cilindrada, asientosXtra):
        super().__init__(color, ruedas, ancho, alto,
                         asientos, marchas, aire, carga, cilindrada)

        self.asientosXtra = asientosXtra

    def getInfo(self):
        return super().getInfo() + f", Asientos Extra: " + str(self.asientosXtra)


class Moto (Coche, Bicicleta):
    def __init__(self, color, ruedas, ancho, alto, asientos, marchas, aire, carga, cilindrada):
        super().__init__(color, ruedas, ancho, alto,
                         asientos, marchas, aire, carga, cilindrada)

    def getInfo(self):
        return super().getInfo()


Vehiculo1 = Vehiculo("Rojo", 4, 120, 145, 5, 5)
Bicicleta1 = Bicicleta("Verde", 2, 20, 60, 1, 6)
Coche1 = Coche("Azul", 4, 200, 250, 5, 6, True, 50, 1000)
Furgoneta1 = Furgoneta("Blanco", 4, 200, 100, 5, 5, True, 300, 900, 2)
Moto1 = Moto("Negro", 2, 60, 100, 2, 6, False, 50, 1300)

print(Vehiculo1.getInfo())
print(Bicicleta1.getInfo())
print(Coche1.getInfo())
print(Furgoneta1.getInfo())
print(Moto1.getInfo())
