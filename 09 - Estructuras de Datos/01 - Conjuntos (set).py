'''set en python
VAN ENTRE { }

Un set es una colección no ordenada de elementos únicos. NO admiten repeticion
- no admite indexación
- no registran la posición de los elementos
- no registran el orden de inserción

Usos:
- Eliminar elementos duplicados
- Comprobacion de existencia de un elemento
- Codigo mas eficiente y legible en menos tiempo.'''

# Da igual que haya elementos repetidos, solo se guardará uno.
sistemaSolar = "Mercurio, Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton, Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton"

# Vamos a agregar a un conjunto vacio cada uno de los planetas.
planetas = set()

for planeta in sistemaSolar.split(", "):
    planetas.add(planeta)

print(planetas)
print(len(planetas))
