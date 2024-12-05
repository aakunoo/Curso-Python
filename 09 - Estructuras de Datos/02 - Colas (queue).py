'''Queues

En una cola se van sumando elementos uno a uno.

Tenemos 3 tipos de colas:
- FIFO (First In First Out): El primer elemento que entra es el primero en salir.
- LIFO (Last In First Out): El último elemento que entra es el primero en salir.
- Priority Queue: Los elementos tienen una prioridad y se ordenan en función de ella. (Son tuplas)

Metodos de las colas:
- put(): Añade un elemento a la cola.
- get(): Devuelve el primer elemento de la cola y lo elimina.
- empty(): Devuelve True si la cola está vacía.
- full(): Devuelve True si la cola está llena.
- qsize(): Devuelve el tamaño de la cola.
- task_done(): Indica que una tarea ha sido completada.
- join(): Espera a que se completen todas las tareas.
- put_nowait(): Igual que put() pero sin esperar a que se complete.
- get_nowait(): Igual que get() pero sin esperar a que se complete.

Para especificar numero maximo de elementos en una cola:
- queue.Queue(3): FIFO
- queue.LifoQueue(3): LIFO
- queue.PriorityQueue(3): Priority
'''

import queue  # importamos la libreria queue

# Creamos una cola FIFO
micola = queue.Queue()
# Incluir elementos en esta cola:
micola.put("Laura")
micola.put("el amor")
micola.put("de mi vida")

# Sacar elementos de la cola
print(micola.get())  # la cola ahora solo tiene "el amor" y "de mi vida"
print("------")

for i in micola.queue:  # imprimimos el resto de elementos de la cola
    print(i)

# --------------------------------------------------------------------------------------------

# Creamos una cola LIFO
micola2 = queue.LifoQueue()

print("\n------------------")

micola2.put("Madrid")
micola2.put("Barcelona")
micola2.put("Sevilla")

print(micola2.get())
print("\nLa cola ahora solo tiene Madrid y Barcelona\n")
for j in micola2.queue:
    print(j)

# --------------------------------------------------------------------------------------------

# Creamos una cola Priority
micola3 = queue.PriorityQueue()

print("\n------------------")

micola3.put((3, "Carcel"))
micola3.put((1, "Casa"))
micola3.put((2, "Trabajo"))

print(micola3.get())
print("\nLa cola ahora solo tiene Casa y Trabajo\n")

for k in micola3.queue:
    print(k)
