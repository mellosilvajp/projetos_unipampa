#o programa lê e adiciona ao vetor os numeros digitados pelo usuario
#em seguida, ele mostra o maior e menor valor contido no vetor e suas respectivas posições


valores = []
maior = menor = 0
for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    for j in valores:
        if j >= maior:
            maior = menor = j
        if j <= menor:
            menor = j
print(f'O maior valor encontrado foi {maior}, nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posicao}...',end='')
print()
print(f'O menor valor encontrado foi {menor}, nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posicao}...', end='')
print()



