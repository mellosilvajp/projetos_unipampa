#http://www.facom.ufu.br/~backes/gbt017/ListaPython07.pdf

#Faça uma funcão recursiva que receba um numero inteiro positivo impar N
# e retorne o fatorial duplo desse numero. O fatorial duplo é definido como
# o produto de todos os numeros naturais ímpares de 1 ate algum numero natural
# ımpar N. Assim, o fatorial duplo de 5 é: 5!!= 5*3*1 = 15


def fatorial_duplo(numero):
    if numero == 1:
        return numero
    else:
        return numero * fatorial_duplo(numero-2)



def main():
    numero = int(input('Digite um número ímpar para ser calculado o seu fatorial duplo: '))
    while numero % 2 == 0:
        print('Você digitou errado.')
        numero = int(input('Digite um número ímpar para ser calculado o seu fatorial duplo: '))
    resultado_fatorial_dp = fatorial_duplo(numero)
    print(resultado_fatorial_dp)


main()
