from tkinter import *
import time

def obtener_palabras(texto):
    estado = 0
    palabras_aceptadas = []
    temporal = ''
    letra_auxiliar = ''
    for x in texto:
        letra_auxiliar = x
        letra_auxiliar.lower()

        estado = automata(estado, letra_auxiliar)

        if estado == -1:
            estado = 0
            temporal = ''
        elif estado == 4:
            palabras_aceptadas.append(temporal)
            estado = 0
            temporal = ''
        else:
            temporal += x

    return palabras_aceptadas

def automata(estado, letra_auxiliar):
    alfabeto = [97, 122]
    if estado == 0:
        return estado_cero(alfabeto,letra_auxiliar)
    elif estado == 1:
        return estado_uno(alfabeto,letra_auxiliar)
    elif estado == 2:
        return estado_dos(alfabeto,letra_auxiliar)
    elif estado == 3:
        return estado_tres(alfabeto,letra_auxiliar)
    else:
        return -1


def estado_cero(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 1
        else:
            return 0
    else:
        return -1


def estado_uno(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 1
        elif letra == 'r':
            return 2
        else:
            return 0
    else:
        return -1


def estado_dos(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 3
        else:
            return 0
    else:
        return -1


def estado_tres(alfabeto,letra):
    if(ord(letra) >= alfabeto[0] and ord(letra) <= alfabeto[1]):
        if letra == 'e':
            return 1
        else:
            return 0
    else:
        return 4

def graficar_automata():
    raiz = Tk()
    raiz.title('Autómata')
    raiz.geometry('500x350')
    canvas = Canvas(raiz, width=600, height=410, bg='white')
    canvas.place(x=0,y=0)
    canvas.pack(expand=YES, fill=BOTH)

    x = 90
    y = 100
    r = 50
    numero_circulos = 4
    opciones = ['e','r','e']
    canvas.create_line(x-20, y+r*1.2, x+.2*r, y+.8*r, width=2, fill='black')
    for i in range(numero_circulos):
        dibujos_especificos(canvas, i, x, y)
        x += r+50

    x = 90
    for i in range(numero_circulos):
        canvas.create_oval(x, y, x+r, y+r, width=1, fill='white')
        widget = Label(canvas, text='q'+str(i), fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+.5*r, y+.5*r, window=widget)

        if i < numero_circulos-1:
            canvas.create_line(x+r, y+(r/2), x+r+50, y+(r/2), width=2, fill='black')
            widget = Label(canvas, text=opciones[i], fg='black', bg='white')
            widget.pack()
            canvas.create_window(x+r+25, y+(r/2)-15, window=widget)
            canvas.create_oval(x+r+40, y+(r/2)-5, x+r+50, y+(r/2)+5, width=1, fill='black')

        if i == numero_circulos -1:
            canvas.create_oval(x+5, y+5, x+r-5, y+r-5, width=1, fill='white')
        x += r+50

    raiz.mainloop()

def dibujos_especificos(canvas, i, x, y):
    if i == 0:
        xy = x+10, y-20, x+30, y+10
        canvas.create_oval(x-30,y-10, x+10,y+20, width=1)
        canvas.create_oval(x-5, y+13, x+5, y+23, width=1, fill='black')
        widget = Label(canvas, text='no es e', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x-20, y-25, window=widget)
    elif i == 1:
        xy = x-75, y-40, x+25, y+40
        canvas.create_arc(xy, start=0, extent=180, style='arc')
        canvas.create_oval(x-80, y-10, x-70, y, width=1, fill='black')
        canvas.create_oval(x+5,y+30, x+45,y+70, width=1)
        widget = Label(canvas, text='no es e ni r', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x-20, y-55, window=widget)
        canvas.create_oval(x+40,y+40, x+50,y+50, width=1, fill='black')
        widget = Label(canvas, text='es e', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+25, y+85, window=widget)
    elif i == 2:
        xy = x-180, y-70, x+20, y+130
        canvas.create_arc(xy, start=0, extent=-180, style='arc')
        widget = Label(canvas, text='no es e', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x-75, y+145, window=widget)
        canvas.create_oval(x-180,y+50, x-170,y+60, width=1, fill='black')
    elif i == 3:
        xy = x-285, y-100, x+20, y+200
        canvas.create_arc(xy, start=0, extent=-180, style='arc')
        canvas.create_oval(x-290,y+45, x-280,y+55, width=1, fill='black')
        widget = Label(canvas, text='no es e', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x-140, y+215, window=widget)
        xy = x-170, y+120, x+20, y-50
        canvas.create_arc(xy, start=0, extent=180, style='arc')
        canvas.create_oval(x-165,y+5, x-155,y-5, width=1, fill='black')
        widget = Label(canvas, text='es e', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x-80, y-65, window=widget)
