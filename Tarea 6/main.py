from btree import ArbolB

print('CONFIGURACION DEL ARBOL B')

grado=int(input('Ingrese grado: '))

arbol=ArbolB(grado)

while True:

    print('\n1.Insertar')
    print('2.Busqueda')
    print('3.Eliminar')
    print('4.Cargar CSV')
    print('5.Generar Grafica')
    print('6.Salir')

    op=input('Seleccione: ')

    if op=='1':
        clave=int(input('Clave: '))
        arbol.insertar(clave)

    elif op=='2':
        clave=int(input('Buscar: '))

        if arbol.buscar(clave):
            print('Encontrado')
        else:
            print('No existe')

    elif op=='3':
        clave=int(input('Eliminar: '))
        arbol.eliminar(clave)

    elif op=='4':
        archivo=input('CSV: ')
        arbol.cargar_csv(archivo)
        print('Carga completada')

    elif op=='5':
        arbol.generar_graphviz()

    elif op=='6':
        break