
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

def raiz_cuadrada_entera(numero):
    def calcular_raiz_cuadrada(num, candidato): 
        if candidato * candidato > num: 
            return candidato - 1 
        return calcular_raiz_cuadrada(num, candidato + 1) 
    return calcular_raiz_cuadrada(numero, 0)

def convertir_a_decimal(romano): 
	valores = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 } 
	def calcular(romano, indice):
		if indice == len(romano) - 1: 
			return valores[romano[indice]] 
		actual = valores[romano[indice]] 
		siguiente = valores[romano[indice + 1]] 
		if actual < siguiente: 
			return -actual + calcular(romano, indice + 1) 
		else: 
			return actual + calcular(romano, indice + 1)
	return calcular(romano, 0)

def suma_numeros_enteros(numero):
    if(numero==0):
        return 0
    return suma_numeros_enteros(numero-1) + numero

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
        romano = input("Numero romano: ")
        print(convertir_a_decimal(romano))

    elif op == "5":
        numero = int(input("Numero hasta el que quiera sumar: "))
        print(suma_numeros_enteros(numero))

    
    elif op == "6":
        break

    else:
        print("Opcion invalida")

