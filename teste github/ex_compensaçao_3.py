#O programa lê um número e:
#se ele for par, é adicionado ao vetor_pares
#mostra quantas vezes foi digitado o valor 9
#mostra o vetor com todos os números digitados pelo usuario
#se tiver o numero 3 no vetor, ele mostra a posição de 3
# se nao, ele diz que o valor 3 nao foi digitado
#exibe os valores pares


vetor = []
vetor_pares = []
for i in range(4):
    numero = int(input('Digite um número: '))
    vetor.append(numero)
    if numero % 2 == 0:
        vetor_pares.append(numero)
print(vetor)
print(f'O valor 9 apareceu {vetor.count(9)} vezes.')
if 3 in vetor:
    print(f'O valor 3 foi digitado na posição {vetor.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os números pares digitados foram: {vetor_pares}')
