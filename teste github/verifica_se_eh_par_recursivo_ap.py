#https://www.math.tecnico.ulisboa.pt/~ccal/python/ex02.html
#
#Defina a função verifica_se_eh_par que recebe como parametro um vetor de números inteiros
# e devolve True se  o vetor  contém um número par e False em caso contrário.

import random

def verifica_se_eh_par(vetor):
    if len(vetor) == 0:
        print(False)
        return False
    if vetor[0] % 2 == 0:
        print(True)
        return True
    if len(vetor) == 1:
        if vetor[0] % 2 != 0:
            print(False)
            return False
    else:
        verifica_se_eh_par(vetor[1:])



def main():
    vetor = []
    for i in range(10):
        #Obs: Para obter apenas números ímpares, basta mudar o "passo" do random.randrange para 2
        numero = random.randrange(1,30,1)
        vetor.append(numero)

    print(vetor)
    verifica_se_eh_par(vetor)

main()
