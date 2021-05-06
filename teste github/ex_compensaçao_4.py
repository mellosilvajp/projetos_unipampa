#o programa exibe, com formatação,o nome e o preço de cada produto ao lado.



vetor_produtos = ['Lápis', 1.75,
                  'Borracha', 2,
                  'Caderno', 15.9,
                  'Estojo', 25,
                   'Transferidor', 4.2,
                  'Mochila', 120.32,
                  'Canetas', 22.3,
                  'Livro', 34.9]
print('-'*10, end='')
print(f'LISTAGEM DE PREÇOS', end='')
print('-'*10)
for i in range(0, len(vetor_produtos)):
    if i % 2 == 0:
        print(f'{vetor_produtos[i]:.<30}', end='')
    else:
        print(f'R${vetor_produtos[i]:>7.2f}')
