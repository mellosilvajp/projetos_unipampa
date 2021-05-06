#https://panda.ime.usp.br/pythonds/static/pythonds_pt/04-Recursao/16-exercicios.html
#Faça um programa recursivo para desenhar árvores usando Turtle
#Modifique a espessura dos ramos para que, quando o tamanho_do_galho ficar menor, a linha fica mais fina.
#Modifique a cor dos ramos para que, quando o tamanho_do_galho ficar muito curto, seja colorido como uma folha..

import turtle

def arvore(tamanho_do_galho,tartaruga,espessura):
    if tamanho_do_galho > 5:
        tartaruga.pensize(espessura)
        tartaruga.forward(tamanho_do_galho)
        tartaruga.color("green")
        tartaruga.right(20)
        arvore(tamanho_do_galho-15,tartaruga, espessura-1)
        tartaruga.left(40)
        arvore(tamanho_do_galho-15,tartaruga, espessura-1)
        tartaruga.right(20)
        tartaruga.backward(tamanho_do_galho)

def main():
    tartaruga = turtle.Turtle()
    janela = turtle.Screen()
    tartaruga.up()
    tartaruga.left(90)
    tartaruga.backward(100)
    tartaruga.down()
    tartaruga.color("brown")
    arvore(75,tartaruga, 6)
    janela.exitonclick()

main()
