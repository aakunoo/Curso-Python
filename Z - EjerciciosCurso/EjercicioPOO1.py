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
        dinero = int(input("Cuanto dinero deseas ingresar?: "))
        self.saldo = self.saldo + dinero

    def retirarDinero(self):
        dinero = int(input("Cuanto dinero deseas retirar?: "))
        self.saldo = self.saldo - dinero


tio1 = CuentaCorriente("12345A", "Jeronimo", 1000)
print("Tu informacion es: " + tio1.getDatos())


pregIngresar = input("\nQuieres ingresar dinero en tu cuenta? (si/no): ")

if pregIngresar == "si":
    tio1.ingresarDinero()
    print("Has ingresado dinero.")
elif pregIngresar == "no":
    print("No has ingresado dinero.")

print("\nTu informacion actualizada es: " + tio1.getDatos())

pregRetirar = input("\nQuieres retirar dinero de tu cuenta? (si/no): ")

if pregRetirar == "si":
    tio1.retirarDinero()
    print("Has retirado dinero.")
elif pregRetirar == "no":
    print("No has retirado dinero.")


print("\nTus datos son: " + tio1.getDatos())
