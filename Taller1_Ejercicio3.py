class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class LDL:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:  # Si la lista ya tiene elementos
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" <-> " if nodo_actual.siguiente else " <-> NULL\n")
            nodo_actual = nodo_actual.siguiente


# Prueba 1:
Lista = LDL()
Lista.encolar(1)
Lista.encolar(5)
Lista.encolar(6)
Lista.encolar(9)
Lista.encolar(10)
Lista.mostrar()
# Respuesta esperada: 1 <-> 5 <-> 6 <-> 9 <-> 10 <-> NULL

# Prueba 2:
Lista = LDL()
Lista.encolar(8)
Lista.encolar(8)
Lista.encolar(10)
Lista.encolar(10)
Lista.encolar(20)
Lista.mostrar()
# Respuesta esperada: 8 <-> 8 <-> 10 <-> 10 <-> 20 <-> NULL

