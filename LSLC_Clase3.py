class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LSLC:
    def __init__(self):
        self.cabecera =None
        self.fin = None

    def InsertarPrimerNodo(self, valor):
        if self.fin !=None: #Si LSLC esta vacia
            return self.fin
        nuevo_nodo=Nodo(valor)
        self.fin=nuevo_nodo
        self.fin.siguiente = self.fin
        self.cabecera=self.fin
        return self.fin

