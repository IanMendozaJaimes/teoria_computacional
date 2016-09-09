import pdb

def evaluar_cadena(texto):
    tabla_estados = [[0]]
    estado = []
    contador = 0
    for x in texto:
        for i in range(len(tabla_estados)):
            estado = automata(tabla_estados[i][contador], x)
            if len(estado) == 2:
                tabla_estados.append([0] * (contador+1))
                tabla_estados[(len(tabla_estados)-1)].append(1)
                tabla_estados[i].append(0)
            elif estado[0] == 2:
                tabla_estados[i].append(2)
            elif estado[0] == -1:
                tabla_estados[i].append(-1)
            else:
                tabla_estados[i].append(0)

        contador += 1

    return tabla_estados

def automata(estado, letra):
    if estado == 0:
        return estado_cero(letra)
    elif estado  == 1:
        return estado_uno(letra)
    elif estado == 2:
        return estado_dos(letra)
    else:
        return [-1]


def estado_cero(letra):
    if letra == '0':
        return [0,1]
    elif letra == '1':
        return [1]
    else:
        return [-1]



def estado_uno(letra):
    if letra == '1':
        return [2]
    else:
        return [-1]



def estado_dos(letra):
    if letra != '':
        return [-1]
    else:
        return [2]



def imprimir_estados(tabla_estados):
    for x in range(0,len(tabla_estados[0])):
        for j in range(len(tabla_estados)):
            if tabla_estados[j][x] == -1:
                print('xx', end=' ')
            else:
                print('q'+str(tabla_estados[j][x]), end=' ')

        print("")
