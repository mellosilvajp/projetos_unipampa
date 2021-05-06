#http://www.facom.ufu.br/~backes/gbt017/ListaPython04.pdf

#Leia uma matriz 4 x 4, imprima a matriz e retorne a localizacao (linha e a coluna) do maior valor.




def enfeita_codigo():
    print('=-'*30)




def inicializa_matriz():
    matriz = [[ 0, 0, 0, 0 ],
              [ 0, 0, 0, 0 ],
              [ 0, 0, 0, 0 ],
              [ 0, 0, 0, 0 ]]
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            matriz[linha][coluna] = int(input(f'Digite um valor para adicionar à matriz na posição [{linha} , {coluna}]: '))
    return matriz



def verifica_maior(matriz):
    maior = 0
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
    return maior




def imprime_matriz(matriz):
    enfeita_codigo()
    for linha in range(0, len(matriz)):
        for coluna in range(0, len(matriz)):
            print(f'{matriz[linha][coluna]:^5}', '  ', end='')
        print()
