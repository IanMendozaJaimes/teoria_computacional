from metodos import *

def main():
    try:
        while True:
            opcion = imprimir_menu()
            texto = ''
            tabla_estados = []
            if opcion == 1:
                texto = input('\n\nIngrese una palabra binaria para evaluar: ')
                tabla_estados = evaluar_cadena(texto)
                imprimir_estados(tabla_estados)
            elif opcion == 2:
                aleatorio = 0
                while True:
                    texto = generar_palabra()
                    print('\n\nSe evaluara la palabra: ', texto)
                    tabla_estados = evaluar_cadena(texto)
                    imprimir_estados(tabla_estados)
                    aleatorio = int(random() * 10) % 2
                    if aleatorio == 0:
                        break
            elif opcion == 3:
                graficar_automata()
            else:
                return 1

    except Exception as e:
        print('Uuups, parece que hubo un problema, ', e)


def imprimir_menu():
    seguir = True
    while seguir:
        try:
            opcion = int(input("\n\nIngrese la opcion que desea: \n1.- Ingresar texto \n2.- Automatico \n3.- Ver gráfico del automata \n4.- Salir\n"))
            return opcion
        except Exception as e:
            print("Por favor, ingrese un dato valido.")


main()
