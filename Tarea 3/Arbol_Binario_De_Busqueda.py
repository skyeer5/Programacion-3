import csv
import graphviz

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    # INSERTAR
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_rec(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_rec(nodo.der, valor)

    # BUSCAR
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izq, valor)
        else:
            return self._buscar_rec(nodo.der, valor)
    # ELIMINAR
    def eliminar(self, valor):
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self._eliminar_rec(nodo.izq, valor)

        elif valor > nodo.valor:
            nodo.der = self._eliminar_rec(nodo.der, valor)

        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq

            temp = self._min_valor(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self._eliminar_rec(nodo.der, temp.valor)

        return nodo

    def _min_valor(self, nodo):
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual
    # VISUALIZAR GRAPHVIZ
    def graficar(self):
        dot = graphviz.Digraph()

        def agregar_nodos(nodo):
            if nodo is not None:
                dot.node(str(nodo.valor))

                if nodo.izq:
                    dot.edge(str(nodo.valor), str(nodo.izq.valor))
                    agregar_nodos(nodo.izq)

                if nodo.der:
                    dot.edge(str(nodo.valor), str(nodo.der.valor))
                    agregar_nodos(nodo.der)

        agregar_nodos(self.raiz)

        dot.render("arbol_binario", format="png", view=True)
    # CONVERTIR A BINARIO
    def mostrar_binario(self):
        def recorrer(nodo):
            if nodo:
                print(f"{nodo.valor} -> {bin(nodo.valor)}")
                recorrer(nodo.izq)
                recorrer(nodo.der)

        recorrer(self.raiz)
