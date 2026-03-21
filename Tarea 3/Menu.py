import Arbol_Binario_De_Busqueda;

def menu():
    arbol = Arbol_Binario_De_Busqueda.ArbolBinarioBusqueda()

    while True:
        print("\n--- MENU ARBOL BINARIO ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde CSV")
        print("5. Visualizar árbol (Graphviz)")
        print("6. Convertir a binario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num = int(input("Número a insertar: "))
            arbol.insertar(num)

        elif opcion == "2":
            num = int(input("Número a buscar: "))
            if arbol.buscar(num):
                print("Número encontrado.")
            else:
                print("Número NO encontrado.")

        elif opcion == "3":
            num = int(input("Número a eliminar: "))
            arbol.eliminar(num)

        elif opcion == "4":
            ruta = input("Ingrese ruta del archivo CSV: ")
            arbol.cargar_csv(ruta)

        elif opcion == "5":
            arbol.graficar()

        elif opcion == "6":
            arbol.mostrar_binario()

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()