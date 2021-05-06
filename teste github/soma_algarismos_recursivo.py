#http://www.facom.ufu.br/~backes/gbt017/ListaPython07.pdf
#Faça um função que some os algarismos de um número informado pelo usuário. Ex: 1256: 1+2+5+6=14


def soma_algarismos(numero):
    if len(numero) <= 1:
        return int(numero[0])
    else:
        return int(numero[0]) + soma_algarismos(numero[1:])



def main():
    numero = str(input("Informe um número:"))
    resultado = soma_algarismos(numero)
    print(resultado)


main()
