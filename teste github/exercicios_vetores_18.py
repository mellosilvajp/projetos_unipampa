#http://www.uft.edu.br/engambiental/prof/catalunha/arquivos/ie/Exercicios.pdf

#Faça um   Programa  que   leia   dois  vetores   com   10   elementos   cada.
# Gere   um   terceiro  vetor   de  20   elementos,  cujos  valores deverão ser
# compostos  pelos  elementos intercalados dos  dois  outros vetores.
def inicializa_vetor_1():
    vetor_1 = []
    print('Informe os valores do primeiro vetor')
    for i in range (0, 10):
        vetor_1.append(int(input('Informe um numero: ')))
    return vetor_1

def inicializa_vetor_2():
    vetor_2 = []
    print('Informe os valores do segundo vetor')
    for i in range (0, 10):
        vetor_2.append(int(input('Informe um numero: ')))
    return vetor_2


def inicializa_vetor_intercalado(vetor_1, vetor_2):
    vetor_intercalado = []
    for i in range (0, 10):
        vetor_intercalado.append(vetor_1[i])
        vetor_intercalado.append(vetor_2[i])
    return vetor_intercalado


def main():

    vetor_1 = inicializa_vetor_1()
    vetor_2 = inicializa_vetor_2()
    vetor_intercalado = inicializa_vetor_intercalado(vetor_1, vetor_2)
    print(vetor_intercalado)


main()
