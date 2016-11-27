from methods_turing_machine import string_handler

def main():
    string = input()
    state = string_handler(string)

    if state == 4:
        print('La cadena es valida')
    else:
        print('La cadena no es valida')

main()
