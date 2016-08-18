def encontrar_primos(numeros_primos, n):
    if n == 1:
        return numeros_primos

    if len(numeros_primos) == 0:
        numeros_primos.append(2)
        
    for x in range(2,n+1):
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
        numeros_primos_binarios.append(bin(x)[2:])
        archivo.write(", " + bin(x)[2:])

    return numeros_primos_binarios


def contar_ceros_unos(numeros_primos_binarios):
    numero_ceros_unos = []
    contador_ceros = 0
    contador_unos = 0
    for x in numeros_primos_binarios:
        contador_unos = 0
        contador_ceros = 0
        for y in x:
            if y == '0':
                contador_ceros += 1
            else:
                contador_unos += 1

        numero_ceros_unos.append([contador_ceros, contador_unos])

    return numero_ceros_unos
