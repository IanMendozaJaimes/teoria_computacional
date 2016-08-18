def iniciar_programa():
    numeros_primos = [2,3,5,7,11]
    numeros_primos_binarios = []
    n = 100
    archivo = open("primos.txt", "w")

    numeros_primos = encontrar_primos(numeros_primos, n)
    numeros_primos_binarios = convertir_primos_a_binarios(numeros_primos, archivo)


def encontrar_primos(numeros_primos, n):
    for x in xrange(2,n+1):
        es_primo = True

        for y in numeros_primos:
            if x%y == 0:
                es_primo = False
                break

        if es_primo:
            numeros_primos.append(x)

    return numeros_primos


def convertir_primos_a_binarios(numeros_primos, archivo):
    numeros_primos_binarios = []
    for x in numeros_primos:
        numeros_primos_binarios.append(int(bin(x)[2:]))
        archivo.write(", " + bin(x)[2:])

    return numeros_primos_binarios
