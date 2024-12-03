class CuentaCorriente:
    numeroCuenta = ""
    titular = ""
    saldo = 0

    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):
        return "Numero de Cuenta: " + self.numeroCuenta + ", Titular: " + self.titular + \
            ", Saldo: " + str(self.saldo)

    def ingresarDinero(self):
        dinero = int(input("\nCuanto dinero deseas ingresar?: "))
        self.saldo = self.saldo + dinero

    def retirarDinero(self):
        dinero = int(input("\nCuanto dinero deseas retirar?: "))
        self.saldo = self.saldo - dinero


class CuentaJoven(CuentaCorriente):

    def __init__(self, numeroCuenta, titular, saldo, bonus_promocion):
        super().__init__(numeroCuenta, titular, saldo)
        self.tiene_bonus = False  # para saber si se aplicó un bonus

        pregbonus = input("Quieres anadir un bonus? (si/no): ")
        if pregbonus.lower() == "si":
            input_bonus = input("Introduce el bonus: ")
            bonus_promocion = int(input_bonus)
            self.saldo += bonus_promocion
            self.bonus_promocion = bonus_promocion
            self.tiene_bonus = True
            print(f"\nHas anadido {bonus_promocion} euros a tu saldo.")
        elif pregbonus.lower() == "no":
            print("\nNo has anadido ningun bonus a tu saldo.")

    def getDatos(self):
        datos = super().getDatos()
        if self.tiene_bonus:  # solo muestra el bonus si se aceptó
            datos += ", Bonus: " + str(self.bonus_promocion)
        return datos

    def getBonus(self):
        if self.tiene_bonus:
            return f"El bonus es de {self.bonus_promocion} euros."
        else:
            return "No se aplicó ningún bonus."


# any es un valor cualquiera
persona1 = CuentaJoven("123456B", "Jero", 2000, any)

persona1.ingresarDinero()
print(persona1.getDatos())
print(persona1.getBonus())
