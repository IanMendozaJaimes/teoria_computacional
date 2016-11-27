from tkinter import *

def draw_graphic():
    window = Tk()
    canvas = Canvas(window, width=650, height=500, bg='white')

    window.title('Autómata WEBAY')
    window.geometry('900x575')

    canvas.place(x=0,y=0)
    canvas.pack(expand=YES, fill=BOTH)

    print_the_others(canvas)
    print_first_oval(canvas)

    window.mainloop()


def print_first_oval(canvas):
    xy = 90, 250, 115, 270
    canvas.create_arc(xy, start=0, extent=270, style='arc')
    canvas.create_oval(110, 255, 120, 265, width=1, fill='black')
    canvas.create_line(70, 340, 110, 300, width=2, fill='black')
    canvas.create_oval(105, 305, 115, 295, width=1, fill='black')

    widget = Label(canvas, text="∑-e-w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(60, 260, window=widget)

    widget = Label(canvas, text="Start", fg='black', bg='white')
    widget.pack()
    canvas.create_window(70, 360, window=widget)

    widget = Label(canvas, text="w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(160, 230, window=widget)

    widget = Label(canvas, text="e", fg='black', bg='white')
    widget.pack()
    canvas.create_window(160, 340, window=widget)

    canvas.create_oval(100, 300, 140, 260, width=1, fill='white')
    widget = Label(canvas, text=1, fg='black', bg='white')
    widget.pack()
    canvas.create_window(120, 280, window=widget)


def print_the_others(canvas):
    x = 220
    text = [["e", "b"],["b", "a", "y"]]
    for i in range(3):
        if i < 2:
            canvas.create_line(x, 190, x+200, 190, width=1, fill='black')
            canvas.create_oval(x+190, 195, x+200, 185, fill='black')
            widget = Label(canvas, text=text[0][i], fg='black', bg='white')
            widget.pack()
            canvas.create_window(x+110, 175, window=widget)

            canvas.create_line(x, 370, x+200, 370, width=1, fill='black')
            canvas.create_oval(x+190, 375, x+200, 365, fill='black')
            widget = Label(canvas, text=text[1][i], fg='black', bg='white')
            widget.pack()
            canvas.create_window(x+110, 355, window=widget)

        print_transitions(i, canvas)
        canvas.create_oval(x,210,x+40,170, width=1, fill='white')
        canvas.create_oval(x,390,x+40,350, width=1, fill='white')

        widget = Label(canvas, text=2+i, fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+20, 190, window=widget)
        widget = Label(canvas, text=5+i, fg='black', bg='white')
        widget.pack()
        canvas.create_window(x+20, 370, window=widget)

        if i == 2:
            canvas.create_oval(x+5,205,x+35,175, width=1, fill='white')

        x = x + 200

    print_last_state(canvas)
    canvas.create_line(x, 370, x-160, 370, width=1, fill='black')
    canvas.create_oval(x, 375, x-10, 365, fill='black')
    widget = Label(canvas, text=text[1][2], fg='black', bg='white')
    widget.pack()
    canvas.create_window(x-90, 355, window=widget)

    canvas.create_oval(x, 390, x+40, 350, width=1, fill='white')
    canvas.create_oval(x+5, 385, x+35, 355, width=1, fill='white')


    widget = Label(canvas, text=8, fg='black', bg='white')
    widget.pack()
    canvas.create_window(x+20, 370, window=widget)


def print_transitions(i, canvas):
    if i == 0:
        print_second_state(canvas)
    elif i == 1:
        print_third_state(canvas)
    elif i == 2:
        print_fourth_state(canvas)
    elif i == 3:
        pass


def print_second_state(canvas):
    canvas.create_line(120, 280, 230, 200, width=1, fill='black')
    canvas.create_line(120, 295, 230, 370, width=1, fill='black')
    canvas.create_oval(225, 190, 255, 150)
    canvas.create_oval(220, 170, 230, 180, fill='black')
    widget = Label(canvas, text='w', fg='black', bg='white')
    widget.pack()
    canvas.create_window(240, 137, window=widget)

    xy = 115, 340, 290, 180
    canvas.create_arc(xy, start = 60, extent = 140, style = 'arc')
    widget = Label(canvas, text="∑-e-w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(177, 168, window=widget)

    canvas.create_line(240, 370, 240, 200, width=1, fill='black')
    canvas.create_oval(235, 210, 245, 220, fill='black')
    widget = Label(canvas, text='w', fg='black', bg='white')
    widget.pack()
    canvas.create_window(250, 280, window=widget)

    canvas.create_oval(205, 400, 235, 370)
    canvas.create_oval(227, 388, 237, 398, width=1, fill='black')
    widget = Label(canvas, text='e', fg='black', bg='white')
    widget.pack()
    canvas.create_window(198, 400, window=widget)

    xy = 110, 380, 250, 250
    canvas.create_arc(xy, start = 160, extent = 160, style = 'arc')
    widget = Label(canvas, text='∑-b-e-w', fg='black', bg='white')
    widget.pack()
    canvas.create_window(150, 391, window=widget)


def print_third_state(canvas):
    xy = 450, 100, 110, 350
    canvas.create_arc(xy, start = 10, extent = 200, style = 'arc', width=1)

    xy = 440, 150, 260, 220
    canvas.create_arc(xy, start = 20, extent = 150, style = 'arc')
    canvas.create_oval(255, 175, 265, 185, fill='black')

    canvas.create_line(440, 200, 250, 360, width=1, fill='black')
    canvas.create_oval(253, 349, 263, 359, fill='black')

    widget = Label(canvas, text="e", fg='black', bg='white')
    widget.pack()
    canvas.create_window(390, 220, window=widget)

    widget = Label(canvas, text="w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(342, 138, window=widget)

    widget = Label(canvas, text="∑-b-e-w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(250, 85, window=widget)

    xy = 440, 330, 250, 400
    canvas.create_line(430, 360, 250, 200, width=1, fill='black')
    canvas.create_arc(xy, start = 200, extent = 150, style = 'arc')
    canvas.create_oval(255, 375, 265, 385, fill='black')
    canvas.create_oval(250, 200, 260, 210, fill='black')
    widget = Label(canvas, text="e", fg='black', bg='white')
    widget.pack()
    canvas.create_window(340, 415, window=widget)

    widget = Label(canvas, text="w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(285, 250, window=widget)

    xy = 97, 230, 440, 460
    canvas.create_arc(xy, start = 150, extent = 190, style = 'arc')

    widget = Label(canvas, text="∑-a-e-w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(230, 440, window=widget)


def print_fourth_state(canvas):
    xy = 640, 100, 260, 270
    canvas.create_arc(xy, start = 0, extent = 180, style = 'arc')
    canvas.create_line(640, 180, 640, 370, width=1, fill='black')
    canvas.create_oval(635, 340, 645, 350, fill='black')

    canvas.create_line(640, 200, 250, 360, width=1, fill='black')

    xy = 655, 20, 115, 470
    canvas.create_arc(xy, start = 10, extent = 180, style = 'arc', width=1)

    widget = Label(canvas, text="w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(460, 85, window=widget)

    widget = Label(canvas, text="a", fg='black', bg='white')
    widget.pack()
    canvas.create_window(650, 265, window=widget)

    widget = Label(canvas, text="e", fg='black', bg='white')
    widget.pack()
    canvas.create_window(592, 235, window=widget)

    widget = Label(canvas, text="∑-a-e-w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(400, 40, window=widget)

    canvas.create_line(630, 360, 250, 200, width=1, fill='black')
    widget = Label(canvas, text="w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(500, 320, window=widget)

    xy = 640, 330, 260, 440
    canvas.create_arc(xy, start = 180, extent = 180, style = 'arc')
    widget = Label(canvas, text="e", fg='black', bg='white')
    widget.pack()
    canvas.create_window(480, 425, window=widget)

    xy = 93, 210, 650, 490
    canvas.create_arc(xy, start = 160, extent = 185, style = 'arc')
    widget = Label(canvas, text="∑-e-w-y", fg='black', bg='white')
    widget.pack()
    canvas.create_window(390, 505, window=widget)


def print_last_state(canvas):
    canvas.create_line(830, 360, 250, 200, width=1, fill='black')

    xy = 835, 160, 95, 540
    canvas.create_arc(xy, start = 170, extent = 180, style = 'arc', width=1)

    widget = Label(canvas, text="w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(740, 320, window=widget)

    widget = Label(canvas, text="∑-e-w", fg='black', bg='white')
    widget.pack()
    canvas.create_window(570, 510, window=widget)

    xy = 830, 330, 260, 450
    canvas.create_arc(xy, start = 180, extent = 190, style = 'arc')

    widget = Label(canvas, text="e", fg='black', bg='white')
    widget.pack()
    canvas.create_window(720, 425, window=widget)
