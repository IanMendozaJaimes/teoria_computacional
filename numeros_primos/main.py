from metodos import *
from random import random

def main():
    archivo = open("primos.txt", "w")
    archivo.write("")
    archivo.close()
    seguir = True
    while seguir:
        print("\n\nSelecciona el modo en que se ejecutara el programa: \n 1.- Automático \n 2.- Manual \n 3.- Salir")
        try:
            seleccion = int(input())
            if seleccion > 0 and seleccion <= 2:
                iniciar_programa(seleccion)
            elif seleccion == 3:
                return 1;
            else:
                raise Exception()
        except Exception as e:
            print("Por favor ingrese un dato valido.")


def iniciar_programa(seleccion=1):
    numeros_primos = []
    numeros_primos_binarios = []
    n = 0

    archivo = open("primos.txt", "a")

    if seleccion == 2:
        n = ingresar_datos()
    else:
        n = int(random() * 1000)
        print("\nFue seleccionado un n = ", n)

    numeros_primos = encontrar_primos(numeros_primos, n)
    numeros_primos_binarios = convertir_primos_a_binarios(numeros_primos, archivo)

    archivo.close()


def ingresar_datos():
    while True:
        try:
            dato_n = int(input("\nIngrese el número límite (desde 1 hasta 1000):"))
            if dato_n > 0 and dato_n <= 1000:
                return dato_n
            else:
                raise Exception()
        except Exception as e:
            print("Por favor ingrese un dato valido")

main()
