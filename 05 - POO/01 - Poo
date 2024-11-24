class Coche():

    # Propiedades / Características.
    ruedas = 4
    largoChasis = 260
    anchoChasis = 130
    arrancado = False

    # Métodos / Comportamientos.
    def arrancar(self):  # self se refiere a objetos de tipo Coche.
        self.arrancado = True

       # pass  # pass es para que no de error si no hay nada en la función.

    def estadoCoche(self):
        if (self.arrancado):
            return "El coche está arrancado."
        else:
            return "El coche está parado."


# Para instanciar un objeto de la clase Coche.
Ferrari = Coche()
Dacia = Coche()

print("Tu coche tiene " + str(Ferrari.ruedas) + " ruedas.")

Ferrari.arrancar()  # Llamamos al método arrancar.
# Esta el Ferrari arrancado? True porque hemos llamado al método arrancar.
print(Ferrari.estadoCoche())
print(Dacia.estadoCoche())
