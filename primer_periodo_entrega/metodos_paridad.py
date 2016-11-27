from tkinter import *

def obtener_paridades(texto):
    archivo = open("historial_paridad.txt", 'a')
    historial = ''
    palabras_permitidas = []
    temporal = ''
    estado = 0
    for x in texto:
        historial = '(q'+str(estado)+', '+x+')-->'
        print(historial, end='')
        archivo.write(historial)
        estado = automata(estado, x)

    historial = 'q'+str(estado)
    print(historial, end='  ')
    archivo.write(historial)
    archivo.write('\n')
    archivo.close()
    if estado == 0:
        return True
    else:
        return False


def automata(estado, letra):
    if estado == 0:
        return estado_cero(letra)
    elif estado == 1:
        return estado_uno(letra)
    elif estado == 2:
        return estado_dos(letra)
    else:
        return estado_tres(letra)


def estado_cero(letra):
    if letra == '1':
        return 1
    elif letra == '0':
        return 2
    else:
        return -1


def estado_uno(letra):
    if letra == '1':
        return 0
    elif letra == '0':
        return 3
    else:
        return -1


def estado_dos(letra):
    if letra == '1':
        return 3
    elif letra == '0':
        return 0
    else:
        return -1


def estado_tres(letra):
    if letra == '1':
        return 2
    elif letra == '0':
        return 1
    else:
        return -1

def ejecuta_diagrama():
    ventana = Tk()
    ventana.title("Autómata")
    ventana.geometry("500x350")
    canvas = Canvas(ventana, width=600, height=410, bg='white')
    canvas.place(x=0,y=0)
    canvas.pack(expand=YES, fill=BOTH)

    x = 140
    y = 70
    r = 50

    dibujos_especificos(x,y, canvas, r)


    for i in range(2):
        canvas.create_oval(x, y, x+r, y+r, width=1, fill="white")
        canvas.create_oval(x, y+r+100, x+r, y+2*r+100, width=1, fill="white")

        widget = Label(canvas, text='q'+str(i), fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+25, y+(r/2), window=widget)

        widget = Label(canvas, text='q'+str(i+2), fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+25, y+2*r+75, window=widget)

        if i == 0:
            canvas.create_oval(x+5, y+5, x+r-5, y+r-5, width=1)

        x += r + 100

    ventana.mainloop()


def dibujos_especificos(x, y, canvas, r):
        canvas.create_oval(x-20, y-20, x+r+170, y+2*r+120)
        canvas.create_oval(x+10, y+10, x+r+140, y+2*r+90)

        canvas.create_oval(x+32, y-7, x+42, y+3, width=1, fill="black")
        canvas.create_oval(x+140, y+17, x+150, y+27, width=1, fill="black")
        canvas.create_oval(x+173, y+140, x+183, y+150, width=1, fill="black")
        canvas.create_oval(x+50.5, y+173, x+60.5, y+183, width=1, fill="black")
        canvas.create_oval(x+17.5, y+50, x+27.5, y+60, width=1, fill="black")
        canvas.create_oval(x-7.3, y+156, x+2.7, y+166, width=1, fill="black")
        canvas.create_oval(x+156.5, y+198, x+166.5, y+208, width=1, fill="black")
        canvas.create_oval(x+197.5, y+33, x+207.5, y+43, width=1, fill="black")

        widget = Label(canvas, text='1', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+100, y-31, window=widget)
        widget = Label(canvas, text='1', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+100, y+26, window=widget)

        widget = Label(canvas, text='1', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+100, y+177, window=widget)
        widget = Label(canvas, text='1', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+100, y+234, window=widget)

        widget = Label(canvas, text='0', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x-30, y+103, window=widget)
        widget = Label(canvas, text='0', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+20, y+103, window=widget)

        widget = Label(canvas, text='0', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+180, y+103, window=widget)
        widget = Label(canvas, text='0', fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+230, y+103, window=widget)
