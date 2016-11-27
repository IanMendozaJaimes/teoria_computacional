#include "methods_pushdown_automaton.h"

int pushdown_automaton_handler(char * string){
    if(*string == '\n'){return 0;}

    struct stack Stack;
    int state = 0;
    int i = 0;

    init_stack(&Stack);
    push(&Stack, 'Z');

    while (*(string + i) != '\n') {
        state = pushdown_automaton(string[i], state, &Stack);
        if(state == -1){return -1;}
        i++;
    }

    if(top_of_stack(&Stack) == 'Z'){return 1;}

    return 0;
}


int pushdown_automaton(char element, int state, struct stack * stack){
    if(state == 0){
        return state0(element, stack);
    }
    else{
        if(state == 1){
            return state1(element, stack);
        }
    }
    return -1;
}


int state0(char element, struct stack * stack){
    if(element == '0'){
        push(stack, 'x');
        return 0;
    }
    else{
        if(element == '1'){
            pop(stack);
        }
        return 1;
    }
    return -1;
}

int state1(char element, struct stack * stack){
    if(element == '1'){
        pop(stack);
        return 1;
    }
    else{
        return -1;
    }
}


void init_stack(struct stack * stack){
    if(stack == NULL){return;}
    stack->top_node = NULL;
    stack->limit = 1000;
    stack->number_elements = 0;
}


int push(struct stack * stack, char element){
    if(stack==NULL){return -1;}
    if(stack->number_elements >= stack->limit){return -1;}

    struct node * new_node = (struct node *)malloc(sizeof(struct node));

    new_node->datum = element;
    new_node->previous_node = stack->top_node;
    stack->top_node = new_node;

    return 2;
}


char pop(struct stack * stack){
    if(stack==NULL){return -1;}
    if(is_empty(stack)){return -1;}

    char auxilliar_datum = 0;
    struct node * auxilliar = NULL;

    auxilliar = (struct node *)malloc(sizeof(struct node));
    auxilliar = stack->top_node;
    auxilliar_datum = auxilliar->datum;
    stack->top_node = auxilliar->previous_node;

    free(auxilliar);
    return auxilliar_datum;
}


int is_full(struct stack * stack){
    if(stack==NULL){return -1;}
    if(stack->number_elements < stack->limit){
        return 0;
    }
    else{
        return 1;
    }
}


int is_empty(struct stack * stack){
    if(stack==NULL){return -1;}
    if(stack->top_node == NULL){
        return 1;
    }
    else{
        return 0;
    }
}


char top_of_stack(struct stack * stack){
    if(stack==NULL){return ' ';}
    if(is_empty(stack)){return ' ';}

    return stack->top_node->datum;
}
