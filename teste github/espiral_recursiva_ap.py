#https://panda.ime.usp.br/pythonds/static/pythonds_pt/04-Recursao/06-visualizacao.html

#Desenhe uma espiral recursiva usando o módulo turtle

import turtle

def desenha_espiral(linha, tamanho_da_linha):
    if tamanho_da_linha > 0:
        linha.forward(tamanho_da_linha)
        linha.right(90)
        desenha_espiral(linha, tamanho_da_linha-5)

def main():
    linha = turtle.Turtle()
    janela = turtle.Screen()
    desenha_espiral(linha, tamanho_da_linha=200)
    janela.exitonclick()

main()
