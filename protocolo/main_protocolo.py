from protocolo import *
from grafico_automata_protocolo import dibujar_grafico_automata
from random import random


def main():
    try:
        while True:
            opcion = imprimir_menu()

            if opcion == 1:
                nombre_archivo = "palabras_generadas.txt"
                archivo = open(nombre_archivo, 'w')
                archivo.close()

                while True:
                    estado_encendido = int(random() * 100) % 3
                    estado = 0
                    if estado_encendido == 1:
                        print('\nEstado de la maquina: Encendido')
                    else:
                        print('\nEstado de la maquina: Apagado')
                        return 1
                    while True:
                        estado = automata_protocolo(estado)
                        if estado == 0:
                            break
            elif opcion == 2:
                dibujar_grafico_automata()
            else:
                return 1


    except Exception as e:
        print('Uuups, parece que hubo un problema: ',e)


def imprimir_menu():
    seguir = True
    while seguir:
        try:
            opcion = int(input("\n\nIngrese la opcion que desea: \n1.- Iniciar \n2.- Ver grafico \n3.- Salir \n"))
            return opcion
        except Exception as e:
            print("Por favor, ingrese un dato valido.")


main()
