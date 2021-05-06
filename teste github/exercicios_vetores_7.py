#em um laço de repetição infinito, o usuario digita quantos valores quiser e esses valores
#são adicionados ao vetor
#ao usuario quebrar o laço de repetição, o programa exibe a quantidade de elemntos digitados pelo usuario e os mostra na ordem reversa
#por fim, o programa diz se foi encontrado o valor 5, e em qual posição do vetor

vetor = []
while True:
    numero = int(input('Digite um valor: '))
    vetor.append(numero)
    escolha = str(input('Você quer continuar (S/N)? ')).upper()
    if escolha == 'N':
        break

print(f'Você digitou {len(vetor)} elementos.')
vetor.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {vetor}')
if 5 in vetor:
    print(f'O número 5 foi encontrado no vetor na posição {vetor.index(5)}')
else:
    print(f'O número 5 não foi encontrado no vetor.')
