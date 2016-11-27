from metodos_paridad import obtener_paridades, ejecuta_diagrama
from random import random

def main():
    archivo = open("historial_paridad.txt","w")
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




def ejecuta_manual():
    while True:
        texto = input('\n\nIntrodusca un número binario: ')
        es_permitida = obtener_paridades(texto)
        opcion = ''

        if es_permitida:
            print('La palabra ', texto, ' es permitida')
        else:
            print('La palabra ', texto, ' no es permitida')

        opcion = input("Quiere ingresar otro número? [s/n]  ")
        if opcion != 's' and opcion != 'S':
            return 1



def ejecuta_automatico():
    limite = 0
    aleatorio = 0
    numero = ''
    i = 0
    seguir = True
    es_permitida = False
    continuar = 0

    while seguir:
        limite = int(random() * 2000) % 1001
        i = 0
        while i < limite:
            aleatorio = int(random() * 10) % 2
            if aleatorio == 0:
                numero += '0'
            else:
                numero += '1'
            i += 1

        print('\n\nSe utilizara la palabra: ', numero)
        es_permitida = obtener_paridades(numero)
        if es_permitida:
            print('La palabra ', numero, ' es permitida')
        else:
            print('La palabra ', numero, ' no es permitida')

        continuar = int(random() * 10) % 2
        if continuar == 0:
            seguir = False
        else:
            seguir = True


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


main()
