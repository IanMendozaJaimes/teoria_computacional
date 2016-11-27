from random import random
from tkinter import *

def evaluar_cadena(texto):
    tabla_estados = [[0]]
    estado = []
    contador = 0
    for x in texto:
        for i in range(len(tabla_estados)):
            estado = automata(tabla_estados[i][contador], x)
            if len(estado) == 2:
                tabla_estados.append([0] * (contador+1))
                tabla_estados[(len(tabla_estados)-1)].append(1)
                tabla_estados[i].append(0)
            elif estado[0] == 2:
                tabla_estados[i].append(2)
            elif estado[0] == -1:
                tabla_estados[i].append(-1)
            else:
                tabla_estados[i].append(0)

        contador += 1
    return tabla_estados


def automata(estado, letra):
    if estado == 0:
        return estado_cero(letra)
    elif estado  == 1:
        return estado_uno(letra)
    elif estado == 2:
        return estado_dos(letra)
    else:
        return [-1]


def estado_cero(letra):
    if letra == '0':
        return [0,1]
    elif letra == '1':
        return [1]
    else:
        return [-1]



def estado_uno(letra):
    if letra == '1':
        return [2]
    else:
        return [-1]



def estado_dos(letra):
    if letra != '':
        return [-1]
    else:
        return [2]



def imprimir_estados(tabla_estados):
    archivo = open('historial_cero_uno.txt', 'a')
    auxiliar = ''
    for x in range(0,len(tabla_estados[0])):
        for j in range(len(tabla_estados)):
            if tabla_estados[j][x] == -1:
                archivo.write('xx ')
                print('xx', end=' ')
            else:
                auxiliar = 'q'+str(tabla_estados[j][x])+' '
                archivo.write(auxiliar)
                print(auxiliar, end='')

        archivo.write('\n')
        print("")

    if tabla_estados[len(tabla_estados)-1][len(tabla_estados[0])-1] == 2:
        archivo.write('La palabra es valida\n\n')
        print("La palabra es valida\n\n")
    else:
        archivo.write('La palabra no es valida\n\n')
        print("La palabra no es valida\n\n")

    archivo.close()

def generar_palabra():
    aleatorio = int(random() * 12) % 11
    aleatorio_cero_uno = 0
    i = 0
    texto = ''
    while i < aleatorio:
        aleatorio_cero_uno = int(random() * 10) % 2
        if aleatorio_cero_uno == 1:
            texto += '1'
        else:
            texto += '0'
        i += 1

    return texto


def graficar_automata():
    raiz = Tk()
    raiz.title('Autómata')
    raiz.geometry('500x250')
    canvas = Canvas(raiz, width=600, height=410, bg='white')
    canvas.place(x=0,y=0)
    canvas.pack(expand=YES, fill=BOTH)

    x = 120
    y = 100
    r = 50
    numero_circulos = 3
    opciones = ['0','1']
    canvas.create_line(x-40, y+(r/2), x, y+(r/2), width=2, fill='black')
    canvas.create_oval(x-10, y+(r/2)-5, x, y+(r/2)+5, width=1, fill='black')

    xy = x+5, y-20, x+45, y+40
    canvas.create_arc(xy, start=0, extent=180, style='arc')
    canvas.create_oval(x, y+(r/2)-27, x+10, y+(r/2)-17, width=1, fill='black')
    widget = Label(canvas, text='0,1', fg='black', bg='white')
    widget.pack()
    canvas.create_window(x+25, y-35, window=widget)

    for i in range(numero_circulos):
        canvas.create_oval(x, y, x+r, y+r, width=1, fill='white')
        widget = Label(canvas, text='q'+str(i), fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+.5*r, y+.5*r, window=widget)

        if i < numero_circulos-1:
            canvas.create_line(x+r, y+(r/2), x+r+70, y+(r/2), width=2, fill='black')
            widget = Label(canvas, text=opciones[i], fg='black', bg='white')
            widget.pack()
            canvas.create_window(x+r+25, y+(r/2)-15, window=widget)
            canvas.create_oval(x+r+60, y+(r/2)-5, x+r+70, y+(r/2)+5, width=1, fill='black')

        if i == numero_circulos -1:
            canvas.create_oval(x+5, y+5, x+r-5, y+r-5, width=1, fill='white')
        x += r+70

    raiz.mainloop()
