def obtener_palabras(alfabeto, texto):
    estado = 0
    palabras_aceptadas = []
    temporal = ''
    letra_auxiliar = ''
    for x in texto:
        letra_auxiliar = x
        letra_auxiliar.lower()

        if estado == 0:
            estado = estado_cero(alfabeto,letra_auxiliar)
        elif estado == 1:
            estado = estado_uno(alfabeto,letra_auxiliar)
        elif estado == 2:
            estado = estado_dos(alfabeto,letra_auxiliar)
        elif estado == 3:
            estado = estado_tres(alfabeto,letra_auxiliar)

        if estado == -1:
            estado = 0
            temporal = ''
        elif estado == 4:
            palabras_aceptadas.append(temporal)
            estado = 0
            temporal = ''
        else:
            temporal += x

    return palabras_aceptadas


def estado_cero(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 1
        else:
            return 0
    else:
        return -1


def estado_uno(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 1
        elif letra == 'r':
            return 2
        else:
            return 0
    else:
        return -1


def estado_dos(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 3
        else:
            return 0
    else:
        return -1


def estado_tres(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 1
        else:
            return 0
    else:
        return 4
