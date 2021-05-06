#https://www.passeidireto.com/arquivo/56813560/listas-em-python-exercicios-iniciais

#Faça uma função que receba uma lista de números armazenados de forma crescente ,
# e dois valores ( limite inferior e limite superior),
# e exiba a sublista cujos elementos são maiores ou iguais  ao  limite inferior e menores ou iguais ao limite superior
def inicializa_vetor(tamanho_do_vetor):
    vetor = []
    for i in range(0, tamanho_do_vetor):
        numero = int(input('Digite um número para adicionar ao vetor: '))
        vetor.append(numero)
    return vetor

def enfeita_codigo():
    print('=-'*30)



def verifica_limites(limite_superior, limite_inferior, vetor):
    while limite_superior <= limite_inferior:
        enfeita_codigo()
        print('Você digitou errado. O limite superior deve ser maior que o inferior. Tente novamente ')
        enfeita_codigo()
    else:
        enfeita_codigo()
        print(vetor[limite_inferior-1:limite_superior])

def main():
    tamanho_do_vetor = int(input('Digite o tamanho do vetor: '))
    vetor = inicializa_vetor(tamanho_do_vetor)
    limite_inferior = int(input('Digite o limite inferior do intervalo: '))
    limite_superior = int(input('Digite o limite superior do intervalo: '))
    verifica_limites(limite_superior, limite_inferior, vetor)

main()

