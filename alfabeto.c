#include "alfabeto.h"

int iniciar_programa(){
  int n = 220;
  int tamanio_alfabeto = 2;
  char * alfabeto = NULL;

  alfabeto = (char *)malloc(tamanio_alfabeto * sizeof(char)); //esto sera nuestro arreglo para el alfabeto

  printf("El numero esperado de combinaciones es: %d\n", potencia(tamanio_alfabeto, n));


  return 1;
}


int potencia(int base, int exponente){
  if(exponente == 0){
    return 1;
  }
  return potencia(base, exponente-1) * base;
}





















/*
0,1,2

0,1,2    3 a la 1
00, 01, 02, 11, 12, 10, 22, 20, 21     3 al 2
000, 001, 002, 010, 011, 012, 020, 021, 022, 100, 101, 102, 110, 111, 112, 120, 121, 122, 200, 201, 202, 210, 211, 212, 220, 221, 222  este es 3 a la 3
*/
