# Problema

A Igreja Presbiteriana Aliança do Retiro começou a fazer lives de suas celebrações durante a Pandemia do Covid 19. Observou-se a possibilidade de automatizar uma etapa mecânica do preparo das lives, que é a criação de sobreposições para Oradores e Hinos cantados.

# Solução Proposta

Inicialmente foi feito um site em PHP qual automatizava essa geração de imagens, porém foi notório que não era necessário um servidor (observado devido a quedas na hospedagem), poderia ser rodado um programa que fizesse isso localmente. 

Foi, portanto, proposto fazer um código em linguagem Python (por ser portátil e simples, além de ser fácil de editar) que gerasse novamente as imagens de sobreposição.

# Etapas de Produção

Foi utilizado Modelo Iterativo Incremental. Separei o projeto em 5 etapas de fatures:

1. Criação das Classes que implementam a geração da imagem.
2. Criação de uma interface por CMD
3. Criação de uma interface gráfica utilizando TKInter.
4. Variação dos parâmetros para manipular a imagem.
5. Portabilização em executável.

# Projeto

## Pré-requisitos

### Linux

Caso seu linux não suporte o tkinter: 
`apt-get install python-tk`
`sudo apt-get install python3-tk-dbg`

## Ferramentas

Serão utilizadas as seguintes ferramentas:

- Python 3
- Pillow (biblioteca usada para geração de imagens)
- OS (biblioteca usada para manipulação de arquivos e de informações do sistema)
- Pyglet (biblioteca necessária para importar fontes)
- TKInter (biblioteca responsável pela interface gráfica)

# Instalação

A seguir segue o tutorial de instalação do programa feito:

## Linux

## MAC OS