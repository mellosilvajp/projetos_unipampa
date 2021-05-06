#http://www.facom.ufu.br/~backes/gbt017/ListaPython07.pdf


#Faça uma função recursiva que receba um numero inteiro positivo N e retorne o fatorial exponencial desse numero.
# Um fatorial exponencial é um inteiro positivo N elevado à potencia de N-1, que por sua vez é elevado
# à potencia de N-2 e assim em diante. Ou seja: n**(n-1**(n-2**(n-3**(n-4))))


def calcula_fatorial_exponencial(numero):
    if numero <=1:
        return 1
    else:
        return numero **calcula_fatorial_exponencial(numero-1)


def main():
    numero = int(input("Informe um número inteiro para ser calculado o seu fatorial exponencial: "))
    calcula_fatorial_exponencial(numero)
    print(calcula_fatorial_exponencial(numero))


main()
