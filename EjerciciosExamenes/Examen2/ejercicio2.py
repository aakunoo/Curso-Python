class Vehiculo():
    num_vehiculos = 0
    
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        Vehiculo.num_vehiculos +=1
        
    def mostrar_datos(self):
        print(f"{self.marca=}, {self.modelo=}, {self.anio=}, {self.kilometraje=}")
        
    def es_antiguo(self, anioActual):
        if ((anioActual - self.anio)) >10:
            return True
        else: 
            return False
            
        

class Coche(Vehiculo):
    
    def __init__(self, marca, modelo, anio, kilometraje, tipo):
        super().__init__(marca, modelo, anio, kilometraje)
        self.tipo = tipo
        
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"{self.tipo=}")
    
Coche1 = Coche("Peugeot", "A55", 2000, 50000, "Coche")

Coche1.mostrar_datos()

print(Coche1.es_antiguo(2024))