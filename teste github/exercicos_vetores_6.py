#o programa adiciona os valores em posições que variam conforme sua grandeza
#assim que o maior numero é adicionado ao vetor, ele é adicionado ao final da lista por ser o maior
#o menor é adicionado no inicio
#ao final do programa, ele exibe o vetor ordenado



vetor = []
tamanho_do_vetor = int(input('Digite o tamanho do vetor que você quer: '))

for i in range(0, tamanho_do_vetor):
    numero = int(input('Digite um valor: '))
    if i == 0 or numero >= vetor[-1]:
        vetor.append(numero)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(vetor):
            if numero <= vetor[posicao]:
                vetor.insert(posicao, numero)
                print(f'Adicionado à posição {posicao} do vetor')
                break
            posicao += 1
print(f'Os valores adicionados na lista, em ordem, foram: {vetor}')
