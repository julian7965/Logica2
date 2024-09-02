class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class LDL:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar_duplicados(self):
        valores_vistos = set()
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor in valores_vistos:
                nodo_anterior = nodo_actual.anterior
                nodo_siguiente = nodo_actual.siguiente
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_siguiente
                if nodo_siguiente:
                    nodo_siguiente.anterior = nodo_anterior
                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_siguiente
                if nodo_actual == self.cola:
                    self.cola = nodo_anterior
            else:
                valores_vistos.add(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

    def ordenar(self, ascendente=True):
        if not self.cabeza:
            return

        intercambio = True
        while intercambio:
            intercambio = False
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                if (ascendente and nodo_actual.valor > nodo_actual.siguiente.valor) or \
                        (not ascendente and nodo_actual.valor < nodo_actual.siguiente.valor):
                    nodo_actual.valor, nodo_actual.siguiente.valor = nodo_actual.siguiente.valor, nodo_actual.valor
                    intercambio = True
                nodo_actual = nodo_actual.siguiente

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.valor, end=" <-> " if nodo_actual.siguiente else " <-> NULL\n")
            nodo_actual = nodo_actual.siguiente

    def ordenar_y_mostrar(self, ascendente=True):
        self.eliminar_duplicados()
        self.ordenar(ascendente)
        self.mostrar()

# Prueba 1:
Lista = LDL()
Lista.insertar(10)
Lista.insertar(8)
Lista.insertar(8)
Lista.insertar(8)
Lista.insertar(9)
Lista.ordenar_y_mostrar(ascendente=True)

# Prueba 2:
Lista = LDL()
Lista.insertar(1)
Lista.insertar(1)
Lista.insertar(1)
Lista.insertar(1)
Lista.insertar(1)
Lista.ordenar_y_mostrar(ascendente=True)

# Prueba 3:
Lista = LDL()
Lista.insertar(8)
Lista.insertar(7)
Lista.insertar(6)
Lista.insertar(-4)
Lista.insertar(-4)
Lista.insertar(-3)
Lista.insertar(-2)
Lista.insertar(-1)
Lista.ordenar_y_mostrar(ascendente=True)

