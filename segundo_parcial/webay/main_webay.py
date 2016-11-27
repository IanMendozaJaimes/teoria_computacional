from methods_webay import string_handler
from graphics_webay import draw_graphic

def main():
    option = print_menu()

    if option == 1:
        pass
    elif option == 2:
        pass
    else:
        draw_graphic()

    string_handler(hola)


def print_menu():
    while True:
        try:
            option = int(input('Introduzca la opcion que desea: \n 1.- Manual \n 2.- Automatico \n 3.- Grafico \n\n'))
            if option >= 1 and option <= 3:
                return option
            else:
                raise Exception
        except Exception as e:
            print("Por favor, ingrese un dato valido")

draw_graphic()
