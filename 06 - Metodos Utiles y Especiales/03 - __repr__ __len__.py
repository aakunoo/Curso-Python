# class Persona():

#    def __init__(self, nombre, apellido, edad):
#        self.nombre = nombre
#        self.apellido = apellido
#        self.edad = edad

# El metodo repr() nos va a dar una representacion en formato texto de nuestro objeto.
# Hay que sobreescribir el metodo __str__ para que nos muestre la informacion que queramos.

#    def __repr__(self):
#        return "Datos de la persona: \n" + "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad)


# p1 = Persona("Jero", "Vicente", 21)
# print(p1)

''' Ejemplo para el uso de --repr--, es mas utilizado para mostrar la informacion de un objeto en un formato mas entendible. '''

import datetime

today = datetime.date.today()  # Nos da la fecha de hoy.

print(str(today))
# Informacion mas precisa. Nos dice la clase de la que proviene esta informacion.
print(repr(today))

'''Ejemplo de uso de __len__. Crear una clase que va a construir una agenda telefonica.
Para poder guardar los contactos, vamos a utilizar un diccionario. '''


class Agenda():
    def __init__(self):
        self.miagenda = {}

    def agregarPersonas(self, nombre, telefono):
        self.miagenda[nombre] = telefono  # miagenda[clave] = valor

    def __len__(self):
        return len(self.miagenda)  # Devuelve la longitud del diccionario.


AgendaTelefonica = Agenda()

AgendaTelefonica.agregarPersonas("Jero", 622468102)
AgendaTelefonica.agregarPersonas("Laura", 612162123)

# Si yo hago esto sin metodo __len__ me devolveria la direccion de memoria del diccionario.
print(len(AgendaTelefonica))
