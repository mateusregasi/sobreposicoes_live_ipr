from tkinter import ttk, font
from tkinter import *

def roundedBox(box, c):
    canvas = Canvas(box)
    canvas.pack()
    canvas.create_oval((0, 0, box.winfo_reqwidth(), box.winfo_reqheight()), fill=c)

class ImageView:

    def __init__(self, params):
        frame = params['f2']
        colors = params['colors']

        # Pega informações de tamanho
        w = frame.winfo_reqwidth()
        h = frame.winfo_reqheight()
        ratio = 0.8

        # Cria a caixa e define a posição
        self.box = Frame(frame, width=w*ratio, height=h*ratio)
        self.box.place(x=w*(1-ratio)/2, rely=(1-ratio)/2)

        roundedBox(self.box, colors['dark gray'])

        # Define o estilo
        self.style(frame, colors)
    
    def style(self, frame, colors):
        self.box.configure(background=colors["light gray"])
        frame.configure(bg=colors["dark gray"])

        