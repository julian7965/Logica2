# Crear una sola clase
# Cola  circular(CC)

class CC:
    def __init__(self, n):
        self.capacidad = n
        self.V = [None] * n  # V= [None None None None None];n=5
        self.primero = self.final = -1  # inician en la posicion -1 para cuando hagamos
        # el proceso de modulo arraque desde la 0

    def ColaVacia(self):
        return self.primero == -1  # La Cola Vacia

    def ColaLlena(self):
        return self.primero == (self.final + 1) % self.capacidad  # La Cola esta llena

    def EncolarCC(self, valor):
        if self.ColaLlena():
            print("La cola esta llena")
            return
        else:
            if self.ColaVacia():
                self.primero = 0
            self.final = (self.final + 1) % self.capacidad
            self.V[self.final] = valor

    def DesencolarCC(self):  ##ESTA FUNCION TIENE UN ERROR , ENCONTRARLO en linea 33
        if self.ColaVacia():
            print("La cola esta vacia")
            return None
        valor_eliminar = self.V[self.primero]
        if self.primero == self.final:
            self.primero = self.final = -1  # Vuelven a las posiciones iniciales
        else:
            self.primero = (self.primero + 1) % self.capacidad
            return valor_eliminar

    def Visualizar(self):
        if self.ColaVacia():
            print("La cola está vacía")
        else:
            Vector = []
            i = self.primero
            while True:
                Vector.append(self.V[i])
                if i == self.final:
                    break
                i = (i + 1) % self.capacidad
            print(Vector)

#Pruebas
Lista = CC(5)
Lista.EncolarCC(7)
Lista.EncolarCC(21)
Lista.EncolarCC(14)
Lista.DesencolarCC()
Lista.DesencolarCC()
Lista.Visualizar()