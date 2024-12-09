class animal():
    num_animal = 0
    def __init__(self, nombre, orden, continentes, alimentacion):
        self.nombre = nombre
        self.orden = orden
        self.continentes = continentes
        self.alimentacion = alimentacion
        animal.num_animal += 1    
        
        
    def datos(self):
        print(f"{self.nombre=}, {self.orden=}, {self.alimentacion=}")
        
    def comprobar_continentes(self, continente):
        return continente in self.continentes
    
class perro(animal):
    
    pedigiri = False
    
    def __init__(self, nombre, orden, continentes, alimentacion, pedigri):
        super().__init__(nombre, orden, continentes, alimentacion)
        self.pedigri = pedigri
    
    def datos(self):
        super().datos()
        print(f"{self.pedigri=}")
        
    def __lt__(self, otro):
        return not self.pedigri and otro.pedigiri
    
    
