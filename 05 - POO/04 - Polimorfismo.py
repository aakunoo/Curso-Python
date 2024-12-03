''' Poliformismo =  Un objeto de programacion 
puede tener multiples formas de comportarse dependiendo de su contexto. '''


class Persona:

    def hablar(self):
        return "La persona está hablando."


class Trabajador(Persona):

    def hablar(self):
        return "El trabajador está hablando."

# Creamos dos metodos iguales en una clase que hereda de otra clase.


class Director(Trabajador):

    def hablar(self):
        return "El director está hablando."


def hazlesHablar(personas):

    # Durante la ejecucion del programa, es persona lo que se comporta de manera diferente.
    for persona in personas:
        print(persona.hablar())


Antonio = Persona()
Maria = Trabajador()
Ana = Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

print("--------------------------------")

listaPersonas = [Antonio, Maria, Ana]
# El metodo hablar() se comporta de manera diferente dependiendo de la clase que lo llame.
hazlesHablar(listaPersonas)
