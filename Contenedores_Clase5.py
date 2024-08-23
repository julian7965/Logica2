#Crear una sola clase
#Cola no circular(CNC)

class CNC:
    def __init__(self, n):
        self.capacidad = n
        self.V =[] #Contenedor vacio

    def ColaVacia(self):
        return len(self.V) == 0 #Retorna un valor Booleano True

    def ColaLlena(self):
        return len(self.V) == self.capacidad #Retorna un valor Booleano True

    def Encolar(self, valor):
        if self.ColaLlena():
            print("La cola esta llena")
            return
        else:
            nueva_lista = self.V + [valor] #Ubicar un nuevo valor en el contenedor
            self.V[:] = nueva_lista #Actualizar el contenedor

    def Desencolar(self):
        if self.ColaVacia():
            print("La cola esta vacia")
            return None
        else:
            primer_eliminado = self.V[0] #Posicion 0 , primero que entra es el primero que sale
            nueva_lista = self.V[1:] #Filtrado
            #Ejemplo
            # V=[2,7,5,10]
            # primer_eliminado = 2
            # nueva_lista =[7,5,10] , actualización de las posiciones
            self.v[:]  = nueva_lista #Actualizar el contenedor
            return self.V

    def Visualizar(self):
        if self.ColaVacia():
            print("La cola esta vacia")
        else:
            Vector=[]
            for x in self.V:
                Vector.append(x) #append -->apilar o alamacenar cada elemento del contenedor
            print(Vector)

#Pruebas


