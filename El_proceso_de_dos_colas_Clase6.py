class A2CC:   #OJO SOLO PARA COLAS CIRCULARES

    def __init__(self,n):
        m = n // 2
        self.total = n
        self.capacidad = m
        self.V = [None]*self.total
        self.P1 = -1
        self.F1 = self.capacidad - 1
        self.P2 = self.capacidad -1
        self.F2 = self.total - 1

    def ColaLLena(self,puntero_inicial,puntero_final):
        #puntero_inicial= puntero para encolar
        #puntero_final= puntero para desencolar

        #Primera parte posicion 0 hasta la posicion m-1
        if puntero_final == (self.capacidad - 1):
            if puntero_inicial == puntero_final:
                return True

        #Segunda parte  posicion m hasta la posicion n-1
        if puntero_final == (self.total - 1):
            if puntero_inicial == puntero_final:
                return True

    def ColaVacia(self,puntero_inicial,puntero_final):

        # Primera parte posicion 0 hasta la posicion m-1
        if puntero_inicial == - 1 and puntero_final == self.capacidad - 1:
          return True

        #Segunda parte  posicion m hasta la posicion n-1
        if puntero_inicial == self.capacidad - 1 and puntero_final == self.total - 1:
            return True

    def Encolar_1(self,valor):
        if self.ColaLLena(self.P1,self.F1) != True: # Si es (True !=True) = False pero si es (False != Verdadero) = True
            self.P1 = (self.P1 + 1 ) % self.capacidad
            self.V[self.P1] = valor
        else:
            print("La Cola 1 esta llena")

    def Encolar_2(self,valor):
        if self.ColaLLena(self.P2,self.F2) != True: # Si es (True !=True) = False pero si es (False != Verdadero) = True
            self.P2 = ((self.P2 - self.capacidad +1 ) % (self.total - self.capacidad)) + self.capacidad
            #P2 = ((P2 - m +1) %(n-m)) + m
            self.V[self.P2] = valor
        else:
            print("La Cola 2 esta llena")

    def Imprimir(self):
        if self.ColaVacia(self.P1,self.F1) == True:
            return None
        if self.ColaVacia(self.P2,self.F2) == True:
            return None
        print("La lista es: ", self.V)

#Pruebas
n=10
Lista = A2CC(n)
Lista.Encolar_1(5)
Lista.Encolar_2(10)
Lista.Encolar_2(7)
Lista.Encolar_2(99)
Lista.Encolar_2(100)
Lista.Encolar_1(220)
Lista.Encolar_1(880)
Lista.Encolar_1(22)


Lista.Imprimir()
