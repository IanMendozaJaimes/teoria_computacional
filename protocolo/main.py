from protocolo import *
from random import random


def iniciar(nombre_archivo):
    palabras_aceptadas = []

    crear_palabras(nombre_archivo)
    retrazar(0)
    palabras_aceptadas = evaluar(nombre_archivo)

    print("Palabras aceptadas:\n" ,palabras_aceptadas)



def main():
    try:
        nombre_archivo = "palabras.txt"
        archivo = open(nombre_archivo, 'w')
        archivo.close()

        while True:
            estado_encendido = int(random() * 100) % 2
            if estado_encendido == 1:
                print('\nEstado de la maquina: Encendido')
                iniciar(nombre_archivo)
            else:
                print('\nEstado de la maquina: Apagado')
                return 1

    except Exception as e:
        print('Uuups, parece que hubo un problema: ',e)



main()
