def obtener_paridades(texto):
    palabras_permitidas = []
    temporal = ''
    estado = 0
    for x in texto:
        print('E', estado, ' ', x, ', ')
        if estado == 0:
            estado = estado_cero(x)
        elif estado == 1:
            estado = estado_uno(x)
        elif estado == 2:
            estado = estado_dos(x)
        else:
            estado = estado_tres(x)

    if estado == 0:
        return True
    else:
        return False
    #     if estado == 4:
    #         if len(temporal) > 0:
    #             palabras_permitidas.append(temporal)
    #         estado = 0
    #         temporal = ''
    #
    #     elif estado > -1:
    #         temporal += x
    #     else:
    #         estado = 0
    #         temporal = ''
    #
    # return palabras_permitidas


def estado_cero(letra):
    if letra == '1':
        return 1
    elif letra == '0':
        return 2
    else:
        return -1


def estado_uno(letra):
    if letra == '1':
        return 0
    elif letra == '0':
        return 3
    else:
        return -1


def estado_dos(letra):
    if letra == '1':
        return 3
    elif letra == '0':
        return 0
    else:
        return -1


def estado_tres(letra):
    if letra == '1':
        return 2
    elif letra == '0':
        return 1
    else:
        return -1
