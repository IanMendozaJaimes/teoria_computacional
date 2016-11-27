from metodos_planetas import get_numbers
from clases_planetas import states_tree

def main():
    numbers = get_numbers(int(input())) #es un diccionario

    for state in numbers:
        print("Estado:",numbers[state])
        arbol = states_tree(numbers[state], [])
        arbol.generate_tree()
        arbol.imprimir_arbol()
        print("===================")


main()
