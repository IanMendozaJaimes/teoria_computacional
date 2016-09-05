#include "alfabeto.h"

int main(int argc, char const *argv[]) {
    char seleccion = '1';
    int continuar = 1;
    int continuar_modalidad = 1;
    int n = 0;
    char seleccion_tiro = ' ';

    srand(time(NULL));

    while(continuar == 1){
        printf("%s\n", "Seleccione la modalidad: \n1.- Automatico \n2.- Manual \n3.- Salir");
        scanf(" %c", &seleccion);

        if(seleccion == '1' || seleccion == '2'){
            continuar_modalidad = 1;
            while (continuar_modalidad == 1) {
                if(seleccion == '1'){
                    n = 1  + (rand()%1000);
                    printf("Se ha seleccionado un n = %d\n", n);
                }
                else{
                    printf("%s ", "Ingrese un n: ");
                    scanf("%d", &n);
                }

                iniciar_programa(n);

                if(seleccion == '2'){
                    printf("%s\n", "Desea ingresar otra n?: s/n");
                    scanf(" %c", &seleccion_tiro);
                    if(seleccion_tiro == 's' || seleccion_tiro == 'S'){
                        continuar_modalidad = 1;
                    }
                    else{
                        continuar_modalidad = 0;
                    }
                }
                else{
                    continuar_modalidad = rand()%2;
                    printf("%d\n", continuar_modalidad);
                }
            }
        }
        else{
            return 1;
        }
    }


    return 0;
}
