from metodos_palindromos import *

def main():
    print(generator(500,True))



def imprimir_menu():
    seguir = True
    while seguir:
        try:
            opcion = int(input("\n\nIngrese la opcion que desea: \n1.- Ingresar una n \n2.- Automatico \n3.- Ver gráfico del automata \n4.- Salir\n"))
            return opcion
        except Exception as e:
            print("Por favor, ingrese un dato valido.")


main()
