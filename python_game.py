import random

# Lista de letras
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
palabras = ["hola", "casa", "chau", "tateti"]

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

# Función para ordenar palabras dentro de la matriz

def orden_random(matriz, palabras):
    tam = len( matriz )
    orden = ["horiz", "vert"]
    for palabra in palabras:
        elecc = random.choice(orden)
        coor = random.randint(1, tam - 1)
        if elecc == "horiz": 
            for i in range( len(palabra) ):
                matriz[coor][i + 1] = palabra[i]
        if elecc == "vert":
            for i in range( len(palabra) ):
                matriz[i + 1][coor] = palabra[i]


# Creación de matriz

n = int(input("Ingrese el tamaño de la matriz: "))

matriz = [[random.choice(letras) for col in range(n + 1)] for row in range(n + 1)]

imprimir_matriz(matriz)

print()

coordenadas(matriz)

imprimir_matriz(matriz)

print()

orden_random(matriz, palabras)

imprimir_matriz(matriz)

print(matriz[0][1])