import random

# Lista de letras
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
palabras = ["111", "2222", "33333", "444444", "5555555"]

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
        matriz[0][i] = str(i)
        matriz[i][0] = str(i) 

# Función para ordenar palabras dentro de la matriz

def orden_random(matriz, palabras):
    tam = len( matriz )                                   
    orden = ["horiz", "vert"]
    coor_ocup = []
    for palabra in palabras:
        palabra_ubicada = 0
        intentos = 0
        tam_p = len(palabra)
        while (palabra_ubicada < 1 and intentos < 10):
            elecc = random.choice(orden)
            coor = random.randint(1, tam - 1)
            despla = random.randint(1, tam - tam_p)
            if elecc == "horiz":
                cont_intentos_horiz = 0
                while cont_intentos_horiz < 10:
                    posib = []
                    cont_ocup = 0
                    # guardo en una lista las posibles coordenadas en la matriz 
                    for i in range( len(palabra) ):
                        posib.append(f'{coor}{despla + i}')
                    # recorro las dos listas, las coordenadas ocupadas y las nuevas, para saber si se pisan
                    for i in range( len(coor_ocup) ):
                        for j in range( len(posib) ):
                            if coor_ocup[i] == posib[j]:
                                cont_ocup = cont_ocup + 1
                    # Si no hay coincidencias la palabra se acomoda en la matriz y se pone 1 en palabra ubicada y se asegura salir del while
                    if cont_ocup == 0: 
                        palabra_ubicada = 1
                        cont_intentos_horiz = 11
                        for i in range( len(palabra) ):
                            coor_ocup.append(f'{coor}{despla + i}')
                            matriz[coor][despla + i] = palabra[i]
                    # Siempre se suma un intento
                    cont_intentos_horiz = cont_intentos_horiz + 1
            if elecc == "vert":
                cont_intentos_vert = 0
                while cont_intentos_vert < 10:
                    posib = []
                    cont_ocup = 0
                    # guardo en una lista las posibles coordenadas en la matriz 
                    for i in range( len(palabra) ):
                        posib.append(f'{despla + i}{coor}')
                    # recorro las dos listas, las coordenadas ocupadas y las nuevas, para saber si se pisan
                    for i in range( len(coor_ocup) ):
                        for j in range( len(posib) ):
                            if coor_ocup[i] == posib[j]:
                                cont_ocup = cont_ocup + 1
                    # Si no hay coincidencias la palabra se acomoda en la matriz y se pone 1 en palabra ubicada y se asegura salir del while
                    if cont_ocup == 0:
                        palabra_ubicada = 1
                        cont_intentos_vert = 11
                        for i in range( len(palabra) ):
                            coor_ocup.append(f'{despla + i}{coor}')
                            matriz[despla + i][coor] = palabra[i]
                    # Siempre se suma un intento
                    cont_intentos_vert = cont_intentos_vert + 1
            # Se suma un intento al while principal
            intentos = intentos + 1


# Creación de matriz

n = int(input("Ingrese el tamaño de la matriz: "))

matriz = [[random.choice(letras) for col in range(n + 1)] for row in range(n + 1)]

# imprimir_matriz(matriz)

print()

coordenadas(matriz)

# imprimir_matriz(matriz)

print()

orden_random(matriz, palabras)

imprimir_matriz(matriz)
