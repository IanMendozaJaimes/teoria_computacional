#include "methods_pushdown_automaton.h"

int print_menu();
void execute_manual();


int main(){
    int option = 0;

    option = print_menu();
    if(option == 1){
        execute_manual();
    }

    return 0;
}


void execute_manual(){
    char string[1001];
    int c;
    int result = 0;

    while ((c = getchar()) != '\n' && c != EOF);
    fgets(string, 1001, stdin);

    result = pushdown_automaton_handler(string);
    if(result == 1){
        printf("%s\n", "La cadena es valida");
    }
    else{
        printf("%s\n", "La cadena no es valida");
    }
}


int print_menu(){
    char option = ' ';
    while (1) {
        printf("%s\n", "Selecciona la opcion que desee: \n 1.- Manual \n 2.- Automatico \n\n");
        fflush(stdin);
        scanf(" %c", &option);

        if(option == '1' || option == '2'){
            return (option - '0');
        }
        else{
            printf("%s\n", "Por favor, introduce una opcion valida \n\n");
        }
    }
}
