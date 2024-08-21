class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.siguiente = None  # Esto es el null en python


class LSL:
  def __init__(self):
    self.cabecera = None

  def insertar(self, valor):
    nuevo_nodo = Nodo(valor)
    if self.cabecera is None:
      self.cabecera = nuevo_nodo  # Ingresar primer nodo
    else:
      nodo_actual = self.cabecera

      while nodo_actual.siguiente:  # Esto python lo toma como nodo_actual.siguiente != None
        nodo_actual = nodo_actual.siguiente  # Asigna espacio de memoria
      nodo_actual.siguiente = nuevo_nodo  # Reemplazar nuevo nodo en el espacio disponible de memoria

  def imprimir(self):
    if self.cabecera is None:
      print("La LSL esta vacia")
    else:
      nodo_actual = self.cabecera

      while nodo_actual:  # Esto python lo toma como nodo_actual != None
        print(nodo_actual.valor, end="->")
        nodo_actual = nodo_actual.siguiente
      print("None")

  def buscar(self, x_obj):
    nodo_actual = self.cabecera
    pos = 0

    while nodo_actual:  # Esto python lo toma como nodo_actual != None
      if nodo_actual.valor == x_obj:
        print("El valor  {:.0f} se encuentra en la posicion {:.0f}".format(nodo_actual.valor,pos))  # {:.0f} valor entero , el cero es los espacios despues de la coma
        return True
      nodo_actual = nodo_actual.siguiente
      pos += 1
    print("El valor no se encontro")
    return False  # El valor no se encontro

  def eliminarinicio(self):
    if self.cabecera is None:
      print("La LSL esta vacia")
      return
    else:
      self.cabecera=self.cabecera.siguiente
      nodo_actual = self.cabecera

  def eliminacioncualquiera(self,x_valor):
    nodo_actual = self.cabecera
    if self.cabecera is None:
        print("La LSL esta vacia")
        return None
    if nodo_actual is not None:
        if nodo_actual.valor == x_valor:
          self.cabecera = nodo_actual.siguiente
          nodo_actual = None
          return
    while nodo_actual is not None:
        if nodo_actual.valor == x_valor:
          break
        previo=nodo_actual
        nodo_actual = nodo_actual.siguiente
    previo.siguiente = nodo_actual.siguiente
    nodo_actual = None

  def intercambio(self,nodo_1,nodo_2):
    nodo_1.valor, nodo_2.valor = nodo_2.valor, nodo_1.valor

  def ordenar(self,opcion):
    if self.cabecera is None or self.cabecera.siguiente is None:
      return
    cambiar= True
    while cambiar==True:
      cambiar = False
      nodo_actual = self.cabecera
      while nodo_actual.siguiente is not None:
        match opcion:
          case "ascendente":
            if nodo_actual.valor > nodo_actual.siguiente.valor:
              self.intercambio(nodo_actual,nodo_actual.siguiente)
              cambiar= True
            nodo_actual = nodo_actual.siguiente
          case "descendente":
             if nodo_actual.valor < nodo_actual.siguiente.valor:
               self.intercambio(nodo_actual,nodo_actual.siguiente)
               cambiar= True
             nodo_actual = nodo_actual.siguiente

  def nodo_medio(self,cab,fin): # Sugerencia: usar self.cabecera como cab para evitar ciclos infinitos
                                #debido a que nodo_medio es una funcion que se utiliza en la funcion
                                #principal buscar binario
    if cab is None:
      return None
    F,L= cab,cab.siguiente
    while L != fin:
      L=L.siguiente
      if L!=fin:
        L = L.siguiente
        F = F.siguiente
    return F

  def buscar_binario(self,x_valor):
    nodo_actual = self.cabecera
    fin= None
    while True:
      H=self.nodo_medio(nodo_actual,fin)
      if H == None:
        return None
      if H.valor == x_valor:
        return print("Valor {:.0f} encontrado en la LSL".format(H.valor))
      elif H.valor<x_valor:
        nodo_actual = H.siguiente
      else:
        fin= H
      if not(fin==None or fin != nodo_actual):
        break
    return print("Valor {:.0f} NO fue encontrado en la LSL".format(x_valor))






#Pruebas
Lista=LSL()
Lista.insertar(2)
Lista.insertar(1)
Lista.insertar(10)
Lista.insertar(24)
Lista.insertar(8)
Lista.imprimir()

Lista.buscar(10)

Lista.ordenar("ascendente")
Lista.imprimir()
Lista.buscar_binario(10)

Lista.eliminarinicio()
Lista.imprimir()

Lista.eliminacioncualquiera(8)
Lista.imprimir()

