from metodos import obtener_paridades
from random import random

def main():
    try:
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




def ejecuta_manual():
    texto = input('Introdusca un número binario: ')
    es_permitida = obtener_paridades(texto)

    if es_permitida:
        print('La palabra ', texto, ' es permitida')
    else:
        print('La palabra ', texto, ' no es permitida')

    return es_permitida




def imprimir_menu():
    while True:
        try:
            opcion = int(input("\n\nEscoja lo que desea: \n1.- Manual \n 2-Automático \n3.- Ver diagrama \n4.- Salir"))
            if opcion >= 1 and opcion <= 4:
                return opcion
            else:
                raise Exception
        except Exception as e:
            print('Por favor, intrudusca un dato válido')


main()
