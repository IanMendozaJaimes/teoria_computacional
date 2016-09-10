from tkinter import *

def dibujar_grafico_automata():
    raiz = Tk()
    raiz.title('Autómata')
    raiz.geometry('450x250')
    canvas = Canvas(raiz, width=600, height=410, bg='white')
    canvas.place(x=0,y=0)
    canvas.pack(expand=YES, fill=BOTH)

    x = 90
    y = 100
    r = 50
    numero_circulos = 2
    opciones = ['Ready', 'Sending']
    canvas.create_line(x-20, y+r*1.2, x+.2*r, y+.8*r, width=2, fill='black')
    canvas.create_oval(x+.2*r - 8, y+.8*r +7, x+.2*r +2 , y+.8*r-3, width=1, fill='black')

    for i in range(numero_circulos):
        if i == 1:
            canvas.create_oval(x+r, y+10, x+2*r, y-30, width=1, fill='white')
            canvas.create_oval(x+r-3, y-10, x+r+7, y, width=1, fill='black')
            widget = Label(canvas, text='time out', fg='black', bg='white')
            widget.pack()
            canvas.create_window(x+2*r, y-r+5, window=widget)
            xy = x-2*r-30, y+80, x+r, y+r-30
            canvas.create_arc(xy, start=0, extent=-180, style='arc')
            widget = Label(canvas, text='ack', fg='black', bg='white')
            widget.pack()
            canvas.create_window(x-r+10, y+95, window=widget)
            canvas.create_oval(x-2*r-33, y+50, x-2*r-23, y+60, width=1, fill='black')


        canvas.create_oval(x, y, x+2*r, y+r, width=1, fill='white')
        widget = Label(canvas, text=opciones[i], fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+r, y+.5*r, window=widget)

        if i < numero_circulos-1:
            canvas.create_line(x+2*r, y+(r/2), x+2*r+70, y+(r/2), width=2, fill='black')
            widget = Label(canvas, text='data in', fg='black', bg='white')
            widget.pack()
            canvas.create_window(x+2*r+35, y+(r/2)-15, window=widget)
            canvas.create_oval(x+2*r+60, y+(r/2)-5, x+2*r+70, y+(r/2)+5, width=1, fill='black')

        if i == 0:
            canvas.create_oval(x+5, y+5, x+2*r-5, y+r-5, width=1, fill='white')

        x += 2*r+70

    raiz.mainloop()



dibujar_grafico_automata()
