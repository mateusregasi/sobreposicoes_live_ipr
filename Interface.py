from Generator import Generator as G
from ImageView import ImageView
from InputFormulary import InputFormulary

from tkinter import PhotoImage
from tkinter import ttk, font
from tkinter import *

class Interface:

    def __init__(self):
        self.params = dict()

        # Inicia a janela
        self.params['window'] = self.win = Tk()
        self.win.title("Gerador de Sobreposição")
        self.win.resizable(False, False)
        
        # Dimensiona a janela
        self.params['w'] = w = self.win.winfo_screenwidth()
        self.params['h'] = h = self.win.winfo_screenheight()
        self.win.geometry(f"{w}x{h}")

        # Define a cor de fundo
        self.initStyle()

        # Criando os conteiners
        self.params['fdim'] = self.fdim = 2/7
        self.params['f1'] = self.f1 = Frame(self.win, width=self.fdim*w, height=h)
        self.f1.place(x=0,y=0)

        self.params['f2'] = self.f2 = Frame(self.win, width=(1-self.fdim)*w, height=h)
        self.f2.place(x=self.fdim*w,y=0)

        # Cria a interface dos conteiners
        form = InputFormulary(self.params)
        image_viewer = ImageView(self.params)

        # # Adiciona imagem
        # self.img = PhotoImage(file="_img/logo.png")
        # self.img_label = Label(self.win, self.img)
        # self.img_label.pack()

        # # Define os estilos
        # self.setStyle()
        
    def initStyle(self):

        # Inicia as cores
        self.params['colors'] = {}
        self.params['colors']["dark gray"] = "#1E201E"
        self.params['colors']["light gray"] = "#3C3D37"
        self.params['colors']["light green"] = "#697565"
        self.params['colors']["black"] = "#000000"
        self.params['colors']["white"] = "#FFFFFF"
        
    def loop(self):
        self.win.mainloop()

    def appBinds(self):
        def keepRatio(e):
            if e.widget is self:
                height = int(e.width / 0.75)
                if e.height != height:
                    self.geometry(f"{e.width}x{height}")

        self.bind('<Configure>', keepRatio)