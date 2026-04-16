from avl import AVL
from utils import graficar

def menu():
    arbol = AVL()

    while True:
        print("\n1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Visualizar")
        print("6. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            arbol.insertar(int(input("Valor: ")))

        elif opcion == "2":
            print(arbol.buscar(int(input("Valor: "))))

        elif opcion == "3":
            arbol.eliminar(int(input("Valor: ")))

        elif opcion == "4":
            break

        elif opcion == "5":
            graficar(arbol)

        elif opcion == "6":
            break

if __name__ == "__main__":
    menu()