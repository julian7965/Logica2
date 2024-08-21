class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente=None
        self.anterior=None

class LDL:
    def __init__(self):
        self.cabecera = None

    def Insertar_al_Inicio(self,valor):
        nuevo_nodo=Nodo(valor)
        nuevo_nodo.siguiente=self.cabecera
        nuevo_nodo.anterior= None
        if self.cabecera is not None:
            self.cabecera.anterior= nuevo_nodo
        self.cabecera=nuevo_nodo

    def Insertar_al_Final(self,valor):
        nuevo_nodo=Nodo(valor)
        if self.cabecera is None:
            self.cabecera=nuevo_nodo
            return
        nodo_actual=self.cabecera
        while nodo_actual.siguiente != None:
            nodo_actual=nodo_actual.siguiente
        nodo_actual.siguiente= nuevo_nodo
        nuevo_nodo.anterior= nodo_actual

    def imprimir(self):
        nodo_actual=self.cabecera
        while nodo_actual != None:
            print(nodo_actual.valor,end="<-->")
            nodo_actual=nodo_actual.siguiente
        print("None")

#Prueba
Lista = LDL()

Lista.Insertar_al_Final(7)
Lista.Insertar_al_Final(17)
Lista.Insertar_al_Final(25)
Lista.imprimir()

#Prueba
Lista_1 = LDL()
Lista_1.Insertar_al_Inicio(8)
Lista_1.Insertar_al_Inicio(10)
Lista_1.Insertar_al_Inicio(17)
Lista1.imprimir()
