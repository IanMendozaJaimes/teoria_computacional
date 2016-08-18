from metodos import *
from random import random

def main():
    archivo = open("primos.txt", "w")
    archivo.write("")
    archivo.close()
    seguir = True
    while seguir:
        print("\n\nSelecciona el modo en que se ejecutará el programa: \n 1.- Automático \n 2.- Manual \n 3.- Salir")
        try:
            seleccion = int(input())
            if seleccion > 0 and seleccion <= 2:
                iniciar_programa(seleccion)
            elif seleccion == 3:
                return 1;
            else:
                raise Exception()
        except Exception as e:
            print("Por favor ingrese un dato válido.")


def iniciar_programa(seleccion=1):
    numeros_primos = []
    numeros_primos_binarios = []
    numero_ceros_unos = []
    n = 0
    continuar = True
    archivo = open("primos.txt", "a")

    while continuar:
        if seleccion == 2:
            n = ingresar_datos("\nIngrese un número límite ( 0 < n <= 1000): ")
        else:
            n = int(random() * 1000)
            print("\nFue seleccionado un n = ", n)

        numeros_primos = encontrar_primos(numeros_primos, n)
        numeros_primos_binarios = convertir_primos_a_binarios(numeros_primos, archivo)
        numero_ceros_unos = contar_ceros_unos(numeros_primos_binarios)

        imprimir_ceros_unos(numero_ceros_unos, numeros_primos)

        if seleccion == 1:
            continuar = int(random() * 100) % 2
        else:
            eleccion = ingresar_datos("\n¿Desea ingresar otra n?  \n1.- Si \n2.- No \n")
            if eleccion != 1:
                continuar = False

    archivo.close()


def ingresar_datos(texto):
    while True:
        try:
            dato_n = int(input(texto))
            if dato_n > 0 and dato_n <= 1000:
                return dato_n
            else:
                raise Exception()
        except Exception as e:
            print("Por favor ingrese un dato válido")


def imprimir_ceros_unos(numero_ceros_unos, numeros_primos):
    contador = 0
    print (numeros_primos)
    print("{ numero primo, numero de unos }")
    while contador < len(numeros_primos):
        print("{",numeros_primos[contador], ",",numero_ceros_unos[contador][1],"}", end=", ")
        contador += 1

main()
