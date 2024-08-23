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
            self.V[:]  = nueva_lista #Actualizar el contenedor
            return self.V

    def EncolarNuevo(self, nuevo_valor): #añadir un nuevo espacio de memoria
        if self.ColaLlena():
            longitud_actual= len(self.V)
            nueva_lista = [None]*(longitud_actual+1) #Solicitar un nuevo espacio de memoria
                                                     #que por defecto es nulo
            for i in range(longitud_actual):
                nueva_lista[i] = self.V[i] #Copia del contenedor

            #Ejemplo
            #V= [5,7,8,10]
            #nueva_lista[None None None None None]
            #nueva_lista[5,7,8,None]

            nueva_lista[longitud_actual] = nuevo_valor #Adicion o encolar el nuevo elemento
            self.V[:] = nueva_lista
        else:
            return self.V

    def Visualizar(self):
        if self.ColaVacia():
            print("La cola esta vacia")
        else:
            Vector=[]
            for x in self.V:
                Vector.append(x) #append -->apilar o alamacenar cada elemento del contenedor
            print(Vector)

#Pruebas Encolar
n=5
Lista = CNC(n)
Lista.Encolar(7)
Lista.Encolar(10)
Lista.Encolar(18)
Lista.Encolar(25)
Lista.Encolar(9)
Lista.Encolar(88) #Solo imprime hasta el 9 por que la cola esta llena
Lista.Visualizar()

#Pruebas Encolar nuevo
Lista.EncolarNuevo(88)
Lista.Visualizar()

#Pruebas Desencolar
Lista.Desencolar()
Lista.Visualizar()
Lista.Desencolar()
Lista.Visualizar()





