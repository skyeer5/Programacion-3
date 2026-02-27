
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

def raiz_cuadrada_entera(n):
    def calcular_raiz_cuadrada(num, candidato): 
        if candidato * candidato > num: 
            return candidato - 1 
        return calcular_raiz_cuadrada(num, candidato + 1) 
    return calcular_raiz_cuadrada(n, 0)

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
        numero = int(input("Numero: "))
        print("La raiz cuadrada entera es: " + str(raiz_cuadrada_entera(numero)))

    elif op == "4":
        numero = int(input("Numero: "))
        print("Raiz ")

    elif op == "6":
        break

    else:
        print("Opcion invalida")

