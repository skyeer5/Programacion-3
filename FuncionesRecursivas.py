
def convertir_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    if(numero <=0):
        return 0
    return contar_digitos(numero//10) + 1

while True:
    print("1. Convertir a Binario")
    print("2. Contar Dígitos")
    print("3. Raíz Cuadrada Entera")
    print("4. Convertir a Decimal desde Romano")
    print("5. Suma de Números Entero")
    print("6. Salir")

    op = input("Opcion: ")

    if op == "1":
        numero = int(input("Numero: "))
        print(convertir_a_binario(numero))

    elif op == "2":
        numero = int(input("Numero: "))
        print("Cantidad de dígitos:  "  + str(contar_digitos(numero)))

    elif op == "3":
        c = input("Carnet a eliminar: ")

    elif op == "4":
        c = input("Carnet a eliminar: ")

    elif op == "6":
        break

    else:
        print("Opcion invalida")

