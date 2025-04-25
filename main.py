from Interface import Interface
import pyglet, os

# Importando fontes que serão necessárias
pyglet.font.add_file('_font/Roboto-Regular.ttf')

app = Interface()
app.loop()


# WIDTH_IMG = 1920
# HEIGHT_IMG = 1080

# while(1):

#     r = int(input("Informe o que deseja fazer: \n\n1) Gerar sobreposição de ministro\n2) Gerar sobreposição de louvor\n>> "))

#     if(r == 1):

#         title = input("Informe o nome do ministro: ").strip()
#         subtitle = input("Informe a ocupação do ministro: ").strip()
#         # title = "Ministro"
#         # subtitle = "Louvor"

#         G.GenerateMinister(WIDTH_IMG, HEIGHT_IMG, "_font/arial.ttf", 34, "_font/arial-italic.ttf", 20,50, 50, 180, 200, 1, 30, 200, title, subtitle)

#     elif(r == 2):

#         title = input("Informe o nome do louvor: ").strip()
#         subtitle = input("Informe a versão do louvor: ").strip()
#         # title = "Louvor"
#         # subtitle = "Versão"

#         G.generateMusic(WIDTH_IMG, HEIGHT_IMG, "_font/arial-bold.ttf", 40, "_font/arial-italic.ttf", 20, 90, 30, 180, 200, 1, 30, 200, title, subtitle)

#     else:
#         print("Opção inválida, tente novamente!")