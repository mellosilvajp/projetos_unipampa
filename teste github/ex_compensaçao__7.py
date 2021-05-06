#o programa lê e adiciona ao vetor a quantidade de numeros que o usuario quiser digitar
#caso o valor já esteja no vetor, o mesmo não é adicionado
#apos o usario quebrar o laço de repetição, o vetor é exibido na sua ordem.


vetor = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in vetor:
        vetor.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Número Duplicado. Não vou adicionar!')
    escolha = str(input('Você quer continuar (S/N)?')).upper()
    if escolha == 'N':
        break
print(sorted(vetor))
