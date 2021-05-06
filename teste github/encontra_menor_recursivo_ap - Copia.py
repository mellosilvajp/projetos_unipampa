#http://www.facom.ufu.br/~backes/gbt017/ListaPython07.pdf

#Crie um programa que contenha uma função recursiva para encontrar o menor valor em um vetor

import random


#Método tradicional (não funcional)
def encontra_menor_valor_tradicional(vetor, menor_valor, primeira_vez = True):
    if len(vetor) <= 1:
        return vetor[0]
    else:
        if primeira_vez:
            menor_valor = vetor[len(vetor)-1]
            return menor_valor
        if vetor[0] < menor_valor:
            menor_valor = vetor[0]
            return menor_valor
        encontra_menor_valor_tradicional(vetor[1:], menor_valor, False)

#Método não tradicional (funcional)
def encontra_menor_valor(vetor, tamanho_vetor):
    if tamanho_vetor <= 1:
        return vetor[0]
    return min(vetor[tamanho_vetor-1], encontra_menor_valor(vetor, tamanho_vetor-1))


def main():
    vetor = []
    for i in range(0, 10):
        numero = random.randint(10, 100)
        vetor.append(numero)
    menor_valor = 0
    print(vetor)
    print()
    #metodo tradicional
    print("Método tradicional: ", encontra_menor_valor_tradicional(vetor, menor_valor))
    print()
    #metodo não tradicional
    tamanho_vetor = len(vetor)
    print("Método não tradicional: ", encontra_menor_valor(vetor, tamanho_vetor))

main()
