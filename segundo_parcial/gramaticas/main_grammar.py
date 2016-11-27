from methods_grammar import grammar

def main():
    string = input()
    parenthesis_handler = grammar()
    string = parenthesis_handler.derivate_string(string)
    print(parenthesis_handler.steps)
    print(string)


main()
