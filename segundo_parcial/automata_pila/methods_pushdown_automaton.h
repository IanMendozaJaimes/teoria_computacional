#ifndef __METHODS_PUSHDOWN_AUTOMATON_H__
#define __METHODS_PUSHDOWN_AUTOMATON_H__

    #include <stdio.h>
    #include <stdlib.h>

    struct node{
        struct node * previous_node;
        char datum;
    };

    struct stack{
        struct node * top_node;
        int limit;
        int number_elements;
    };

    void init_stack(struct stack *);
    int push(struct stack *, char);
    char pop(struct stack *);
    int is_full(struct stack *);
    int pushdown_automaton_handler(char *);
    int pushdown_automaton(char, int, struct stack *);
    int is_empty(struct stack *);
    int state0(char, struct stack *);
    int state1(char, struct stack *);
    char top_of_stack(struct stack *);

#endif
