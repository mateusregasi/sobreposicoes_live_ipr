from Generator import Generator as G

WIDTH = 1920
HEIGHT = 1080

while(1):

    r = int(input("Informe o que deseja fazer: \n\n1) Gerar sobreposição de ministro\n2) Gerar sobreposição de louvor\n>> "))

    if(r == 1):

        title = input("Informe o nome do ministro: ").strip()
        subtitle = input("Informe a ocupação do ministro: ").strip()
        # title = "Ministro"
        # subtitle = "Louvor"

        G.GenerateMinister(WIDTH, HEIGHT, "arial.ttf", 34, "arial-italic.ttf", 20,50, 50, 180, 200, 1, 30, 200, title, subtitle)

    elif(r == 2):

        title = input("Informe o nome do louvor: ").strip()
        subtitle = input("Informe a versão do louvor: ").strip()
        # title = "Louvor"
        # subtitle = "Versão"

        G.generateMusic(WIDTH, HEIGHT, "arial-bold.ttf", 40, "arial-italic.ttf", 20, 90, 30, 180, 200, 1, 30, 200, title, subtitle)

    else:
        print("Opção inválida, tente novamente!")