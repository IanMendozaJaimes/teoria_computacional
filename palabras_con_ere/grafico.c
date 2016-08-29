
#include <stdio.h>
#include <ncurses.h>

//http://askubuntu.com/questions/525051/how-do-i-use-graphics-h-in-ubuntu
//quisa py27-readline


/*
int dibujar_grafico() {
    int gd = DETECT, gm;
    //initialization of graphic mode
    initgraph(&gd, &gm, "C:\\TC\\BGI");
    line(100,100,200, 200);
    closegraph();
    return 0;
}
*/

int main() {
       initscr();
       printw("Hola linux!");
       refresh();
       getch();
       endwin();
       return 0;
}

int multiplicar(int a, int b){
    return (a * b);
}
