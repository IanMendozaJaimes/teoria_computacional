/*

No podemos saber lo que nos depara el mañana, pero si podemos asegurar que una
transformación lineal es inyectiva si y solo si el único elemento de su kernel es el cero vector

*/
#include "alfabeto.h"

int iniciar_programa(){
  int n = 3;
  int tamanio_alfabeto = 3;
  char * alfabeto = NULL;

  alfabeto = (char *)malloc(tamanio_alfabeto * sizeof(char)); //esto sera nuestro arreglo para el alfabeto
  iniciar_alfabeto(&alfabeto, tamanio_alfabeto);

  obtener_cadenas(alfabeto, tamanio_alfabeto, n);

  return 1;
}


int obtener_cadenas(char *alfabeto, int tamanio, int n){
    int i;
    int j;
    int * cadena_temporal = NULL;
    int salir = 0;
    FILE *archivo = NULL;

    archivo = fopen("cadenas.txt", "w");
    if (archivo == NULL) {
		printf("%s\n", "Error al abrir el archivo");
		exit(0);
	}

    fputs("∑ = { ε", archivo);

    for(i = 1; i <= n; i++){
        cadena_temporal = (int*)calloc(i, sizeof(int));
        while(salir == 0){
            escribir_palabra(&archivo, cadena_temporal, alfabeto, i);
            for(j = i -1; j > -1; j--){
                *(cadena_temporal + j) = *(cadena_temporal + j) + 1;
                if( *(cadena_temporal + j) > (tamanio -1)){
                    *(cadena_temporal + j) = 0;
                }
                else{break;}
            }
            if(j == -1){
                free(cadena_temporal);
                break;
            }
        }
    }
    fputs(" }", archivo);

    return 1;
}

int escribir_palabra(FILE **archivo, int * cadena_temporal, char * alfabeto, int tamanio){
    int i;
    fputs(", ", *archivo);
    for(i = 0; i < tamanio; i++){
        fputc(*(alfabeto + *(cadena_temporal + i)) , *archivo);
    }
    return 1;
}

int iniciar_alfabeto(char **alfabeto, int tamanio){
    int i;
    for(i = 0; i < tamanio; i++){
        *(*alfabeto + i) = i + '0';
    }
    return  1;
}





















/*
0,1,2

0,1,2    3 a la 1
00, 01, 02, 11, 12, 10, 22, 20, 21     3 al 2
000, 001, 002, 010, 011, 012, 020, 021, 022, 100, 101, 102, 110, 111, 112, 120, 121, 122, 200, 201, 202, 210, 211, 212, 220, 221, 222  este es 3 a la 3
*/
