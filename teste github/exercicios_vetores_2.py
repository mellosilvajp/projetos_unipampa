#O programa exibe o maior e menor valor sorteado dentro do vetor


import random

vetor = []
maior = menor = 0
for i in range(0,5):
    numero = random.randint(0,100)
    vetor.append(numero)
    if numero > maior:
        maior = menor = numero
    if numero < menor:
        menor = numero
print(f'Os valores sorteados foram: {vetor[:]}')
print(f'O maior valor encontrado foi: {maior}')
print(f'O menor valor encontrado foi: {menor}')
