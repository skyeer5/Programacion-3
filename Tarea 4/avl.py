from abb import ABB, Nodo

class AVL(ABB):

    def altura(self, nodo):
        if nodo is None:
            return 0
        return max(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1

    def balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)