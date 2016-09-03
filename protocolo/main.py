from protocolo import *
from random import random


def iniciar():
    nombre_archivo = "palabras.txt"
    palabras_aceptadas = []

    archivo = open(nombre_archivo, 'w')
    archivo.close()

    crear_palabras(nombre_archivo)
    retrazar(0)
    palabras_aceptadas = evaluar(nombre_archivo)

    print(palabras_aceptadas)



def main():
    try:
        while True:
            opcion = imprimir_menu()

            if opcion == 1:
                ejecuta_manual()
            elif opcion == 2:
                ejecuta_automatico()
            elif opcion == 3:
                ejecuta_diagrama()
            else:
                return 1

    except Exception as e:
        print('Uuups, parece que hubo un problema: ',e)



def imprimir_menu():
    while True:
        try:
            opcion = int(input("\n\n\nEscoja lo que desea: \n1.- Manual \n2.- Automático \n3.- Ver diagrama \n4.- Salir\n\n"))
            if opcion >= 1 and opcion <= 4:
                return opcion
            else:
                raise Exception
        except Exception as e:
            print('Por favor, intrudusca un dato válido')








iniciar()
