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

    def InsertaralInicio(self, valor):
        if self.fin ==None:
            return self.InsertarPrimerNodo(valor)
        nuevo_nodo=Nodo(valor)
        nuevo_nodo.siguiente = self.fin.siguiente #Generar un nuevo espacio de memoria
        self.fin.siguiente = nuevo_nodo #Colocar el nodo en el nuevo espacio de memoria
        return self.fin

    def InsertarAlFinal(self, valor):
        if self.fin == None:
            return self.InsertarPrimerNodo(valor)
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.fin.siguiente  # Generar un nuevo espacio de memoria
        self.fin.siguiente = nuevo_nodo  # Colocar el nodo en el nuevo espacio de memoria
        self.fin = nuevo_nodo #Colocar el nuevo nodo en el puntero fin
        return self.fin

    def Imprimir(self):
        if self.fin == None:
            print("La LSLC esta vacia")
            return
        nodo_actual=self.fin.siguiente #Se va ubicar en el ultimo metodo (Si utilizamos el metodo de insertar al inicio)
                                       # Se va ubicar en el ultimo metodo (Si utilizamos el metodo de insertar al final)
        while nodo_actual != None:
            print(nodo_actual.valor,end="->")
            nodo_actual=nodo_actual.siguiente
            if nodo_actual == self.fin.siguiente:
                break #Detiene la impresion
        print("None")

#Pruebas
Lista=LSLC()
Lista.InsertaralInicio(11) #cabecera
Lista.InsertaralInicio(9)
Lista.InsertaralInicio(7)
Lista.InsertaralInicio(4)
Lista.Imprimir()

Lista.InsertarAlFinal(15)
Lista.InsertarAlFinal(18)
Lista.InsertarAlFinal(20)
Lista.Imprimir()