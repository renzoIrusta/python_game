import random

# Lista de letras
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Función imprimir matriz

def imprimir_matriz(matriz):
    for f in matriz:
        for c in f:
            print(f"{c:3}", end="")
        print()

# Función crear coordenadas

def coordenadas(matriz):
    tam = len( matriz )
    for i in range(tam):
        matriz[0][i] = i
        matriz[i][0] = i



# Creación de matriz
# 
n = int(input("Ingrese el tamaño de la matriz: "))

matriz = [[random.choice(letras) for col in range(n + 1)] for row in range(n + 1)]

imprimir_matriz(matriz)

print()

coordenadas(matriz)

imprimir_matriz(matriz)