#http://www.facom.ufu.br/~backes/gbt017/ListaPython07.pdf

#Faça uma funcao recursiva que receba um numero inteiro positivo N e retorne o
# super-fatorial desse numero. O superfatorial de um numero N é definida pelo produto dos N
# primeiros fatoriais de N. Assim, o superfatorial de 4 é: sf(4) = 1! ∗ 2! ∗ 3! ∗ 4! = 288


def calcula_fatorial(numero):
    if numero <= 1:
        return numero
    else:
        return numero * calcula_fatorial(numero-1)

def calcula_super_fatorial(numero):
    if numero <=1:
        return numero
    else:
        return calcula_fatorial(numero) * calcula_super_fatorial(numero-1)

def main():
    numero = int(input('Digite um número para calcular o seu fatorial e superfatorial: '))
    resultado_fatorial = calcula_fatorial(numero)
    resultado_super_fatorial = calcula_super_fatorial(numero)
    print("Fatorial: ", resultado_fatorial)
    print("Superfatorial: ", resultado_super_fatorial)


main()
