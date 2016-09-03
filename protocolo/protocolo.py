from random import random
import time

def crear_palabras(nombre_archivo):
    archivo = open(nombre_archivo, "a")
    longitud = 32
    aleatorio_numero = 0
    for x in range(0,10):
        i = 0
        par = int(random() * 10) % 2
        while  i < longitud:
            aleatorio_numero = int(random() * 10) % 2
            if par == 0:
                archivo.write(str(aleatorio_numero)*2)
                i += 2
            else:
                archivo.write(str(aleatorio_numero))
                i += 1
        archivo.write(" ")
    archivo.close()


def retrazar(tiempo):
    time.sleep(tiempo)


def evaluar(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    palabras_permitidas = []
    temporal = ''
    estado = 0
    letra = ''
    while True:
        letra = archivo.read(1)
        if not letra:
            break

        if letra != ' ':
            estado = automata(estado, letra)
            temporal += letra
        else:
            if estado == 0:
                palabras_permitidas.append(temporal)
            estado = 0
            temporal = ''

    return palabras_permitidas

def automata(estado, x):
    if estado == 0:
        return estado_cero(x)
    elif estado == 1:
        return estado_uno(x)
    elif estado == 2:
        return estado_dos(x)
    else:
        return -1



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
