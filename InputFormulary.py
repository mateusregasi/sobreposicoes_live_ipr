from tkinter import ttk, font
from tkinter import *

class InputFormulary():

    def __init__(self, params):
        frame = params['f1']
        colors = params['colors']
        fdim = params['fdim']

        # Posiocionando notebooks
        self.note = ttk.Notebook(frame)
        self.note.place(relwidth=0.8, relheight=0.8)
        self.note.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Criando as abas
        self.tab1 = Frame(self.note)
        self.note.add(self.tab1,text="Ministro")

        self.tab2 = Frame(self.note)
        self.note.add(self.tab2, text="Louvor")

        # Define o estilo
        self.style(frame, colors)
        

    def style(self, frame, colors):

        # Altera a cor de fundo das abas
        self.tab1.configure(background=colors["light gray"])
        self.tab2.configure(background=colors["light gray"])

        frame.configure(bg=colors["dark gray"])
        # ttk.Style().configure("Notebook",
#    background=colors["light gray"])
