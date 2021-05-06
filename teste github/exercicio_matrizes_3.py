#http://www.facom.ufu.br/~backes/gbt017/ListaPython04.pdf

#Declare uma matriz 5 x 5.
# Preencha com 1 a diagonal principal e com 0 os demais elementos.
# Escreva ao final a matriz obtida.



def adiciona_valores_matriz():

    matriz = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            if coluna == linha:
                matriz[linha][coluna] = 1

    return matriz

def imprime_matriz(matriz):
    print('=-'*30)
    print(f'{"MATRIZ":^60}')
    print('=-'*30)
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            print(f'{matriz[linha][coluna]:^5}', '  ', end='')
        print()


def main():

    matriz = adiciona_valores_matriz()
    imprime_matriz(matriz)



main()
