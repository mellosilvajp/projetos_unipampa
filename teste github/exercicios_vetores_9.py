vetor = []
maior = 0
menor = 0
for i in range(0,5):
    vetor.append((int(input(f'Digite um número para a posição {i}:\n'))))
    if i == 0:
        maior = menor = vetor[i]
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print('=-'*30)
print('Vetor:',vetor)
print('=-'*30)
print(f'O maior número é: {maior}, na(s) posição(s):', end='')
for p, v in enumerate(vetor):
    if v == maior:
       print(f'{p}...')
print('=-'*30)
print(f'O menor número é: {menor}, na(s) posição(s):', end='')
for p,v in enumerate(vetor):
    if v == menor:
        print(f'{p}...', end='')
print()
