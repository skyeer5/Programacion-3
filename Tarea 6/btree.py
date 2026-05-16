from graphviz import Digraph
import csv

class NodoB:
    def __init__(self, hoja=False):
        self.hoja=hoja
        self.claves=[]
        self.hijos=[]

class ArbolB:

    def __init__(self,t):
        self.raiz=NodoB(True)
        self.t=t

    def buscar(self,k,x=None):

        if x is None:
            x=self.raiz

        i=0
        while i<len(x.claves) and k>x.claves[i]:
            i+=1

        if i<len(x.claves) and x.claves[i]==k:
            return True

        if x.hoja:
            return False

        return self.buscar(k,x.hijos[i])


    def insertar(self,k):

        raiz=self.raiz

        if len(raiz.claves)==(2*self.t)-1:
            temp=NodoB()
            self.raiz=temp
            temp.hijos.insert(0,raiz)
            self.dividir(temp,0)
            self.insertar_no_lleno(temp,k)

        else:
            self.insertar_no_lleno(raiz,k)


    def insertar_no_lleno(self,x,k):

        i=len(x.claves)-1

        if x.hoja:
            x.claves.append(None)

            while i>=0 and k<x.claves[i]:
                x.claves[i+1]=x.claves[i]
                i-=1

            x.claves[i+1]=k

        else:
            while i>=0 and k<x.claves[i]:
                i-=1

            i+=1

            if len(x.hijos[i].claves)==(2*self.t)-1:
                self.dividir(x,i)

                if k>x.claves[i]:
                    i+=1

            self.insertar_no_lleno(x.hijos[i],k)


    def dividir(self,padre,i):

        t=self.t
        y=padre.hijos[i]
        z=NodoB(y.hoja)

        print('Imagen generada en salida/arbol.png')
    
    def generar_graphviz(self):

        dot=Digraph()

        def recorrer(nodo,id_nodo=0):

            nombre=str(id_nodo)
            etiqueta=' | '.join(map(str,nodo.claves))

            dot.node(nombre,etiqueta)

            contador=id_nodo+1

            for h in nodo.hijos:
                hijo=str(contador)
                dot.edge(nombre,hijo)
                contador=recorrer(h,contador)

            return contador

        recorrer(self.raiz)

        dot.render(
            'salida/arbol',
            format='png',
            cleanup=True
        )