#http://www.facom.ufu.br/~backes/gbt017/ListaPython04.pdf

#Leia uma matriz 4 x 4, conte e escreva os valores maiores que 10 que ela possui.




def inicializa_vetor_e_matrizes(matriz_a, contador, vetor_maiores_que_10):

    for linha in range(0, len(matriz_a)):
        for coluna in range(0, len(matriz_a)):
            numero = int(input(f'Digite um número para adicionar na posição [{linha},{coluna}] da matriz: \n'))
            matriz_a[linha][coluna] = numero
            if matriz_a[linha][coluna] > 10:
               contador += 1
               vetor_maiores_que_10.append(matriz_a[linha][coluna])
    enfeita_codigo()
    print('O total de números maior que 10 é: ', contador)



def mostra_maiores_que_10(vetor_maiores_que_10, matriz_a):
    print('Os números maiores que 10 na matriz são: ', end='')

    for i in range(0, len(vetor_maiores_que_10)):
        print(vetor_maiores_que_10[i], '...', end='')
    print()
    enfeita_codigo()
    for linha in range(0, len(matriz_a)):
        for coluna in range(0, len(matriz_a)):
            print(f'{matriz_a[linha][coluna]:^5}', ' ', end='')
        print()



def enfeita_codigo():
    print('=-'*30)


def main():
    matriz_a = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

    vetor_maiores_que_10 = []

    contador = 0

    inicializa_vetor_e_matrizes(matriz_a, contador, vetor_maiores_que_10)
    mostra_maiores_que_10(vetor_maiores_que_10, matriz_a)




main()
