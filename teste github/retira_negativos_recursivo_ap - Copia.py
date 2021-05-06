#https://www.math.tecnico.ulisboa.pt/~ccal/python/ex02.html

#Defina a função retira_negativos que recebe como parametro um vetor de números inteiros
# e devolve o vetor resultante apenas com os números positivos do vetor .

import random


def retira_negativos(vetor, vetor_resultante):
    if len(vetor) <= 1:
        if vetor[0] >= 0:
            vetor_resultante.append(vetor[0])
            return vetor[0]
        return vetor[0]
    else:
        if vetor[0] >= 0:
            vetor_resultante.append(vetor[0])
        return retira_negativos(vetor[1:], vetor_resultante)


def main():
    vetor = []
    vetor_resultante = []
    for i in range(0, 10):
        numero = random.randint(-50,50)
        vetor.append(numero)
    retira_negativos(vetor, vetor_resultante)
    print("Vetor com todos os números: ", vetor)
    print("Vetor com os números apenas positivos:", vetor_resultante)


main()
