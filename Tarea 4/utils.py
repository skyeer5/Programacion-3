from graphviz import Digraph

def graficar(arbol):
    dot = Digraph()

    def recorrer(nodo):
        if nodo:
            dot.node(str(nodo.valor))
            if nodo.izquierda:
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                recorrer(nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                recorrer(nodo.derecha)

    recorrer(arbol.raiz)
    dot.render('arbol', view=True)