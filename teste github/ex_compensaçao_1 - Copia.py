#O programa exibe o número digitado por extenso

numeros_por_extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                       'dezenove', 'vinte']

while True:
    print('='*30)
    numero_de_entrada = int(input('Digite um número inteiro de 0 a 20: '))
    if numero_de_entrada in range(0,21):
        print(f'Você digitou o número {numeros_por_extenso[numero_de_entrada]}.')
    elif numero_de_entrada > 20 or numero_de_entrada < 0:
        print('Você digitou errado.')
    print('='*30)
    escolha = str(input('VC QUER CONTINUAR(S/N)? '))
    if escolha == 'N' or escolha == 'n':
        break
print('Você encerrou o programa.')




