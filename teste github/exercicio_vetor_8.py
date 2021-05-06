#http://www.uft.edu.br/engambiental/prof/catalunha/arquivos/ie/Exercicios.pdf

#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
def inicializa_vetor_1():
    vetor_1 = []
    print('Informe os valores do primeiro vetor')
    for i in range (0, 10):
        vetor_1.append(int(input('Informe um número: ')))
    return vetor_1


def inicializa_vetor_2():
    vetor_2 = []
    print('Informe os valores do segundo  vetor')
    for i in range (0, 10):
        vetor_2.append(int(input('Informe um número: ')))
    return vetor_2


def inicializa_vetor_3():
    vetor_3 = []
    print('Informe os valores do terceiro vetor')
    for i in range (0, 10):
        vetor_3.append(int(input('Informe um número: ')))
    return vetor_3

def inicializa_vetor_4(vetor_1, vetor_2, vetor_3):
    vetor_4 = []
    for i in range (0, 10):
        vetor_4.append(vetor_1[i])
        vetor_4.append(vetor_2[i])
        vetor_4.append(vetor_3[i])

    return vetor_4



def main():
    vetor_1 = inicializa_vetor_1()
    vetor_2 = inicializa_vetor_2()
    vetor_3 = inicializa_vetor_3()
    vetor_4 = inicializa_vetor_4(vetor_1, vetor_2, vetor_3)
    print(vetor_4)




main()

