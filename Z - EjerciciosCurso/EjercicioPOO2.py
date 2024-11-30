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

    def __init__(self, numeroCuenta, titular, saldo, bonus_promocion=200):
        super().__init__(numeroCuenta, titular, saldo)

        pregbonus = input("Quieres anadir un bonus? (si/no): ")
        if pregbonus == "si":
            self.saldo = int(bonus_promocion) + int(saldo)
            print(f"\nHas anadido {bonus_promocion} euros a tu saldo.")
        elif pregbonus == "no":
            print("\nNo has anadido ningun bonus a tu saldo.")

    def getBonus(self):
        return self.bonus_promocion


persona1 = CuentaJoven("123456B", "Jero", 2000)

persona1.ingresarDinero()
print(persona1.getDatos())
