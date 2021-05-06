#http://www.facom.ufu.br/~backes/gbt017/ListaPython07.pdf

#Faça uma funcão recursiva que calcule o valor da serie S descrita a seguir
# para um valor n > 0 a ser fornecido como parametro para a mesma.

#S = 2 + 5/2 + 10/3 + ... + (1 + n**2)/n

#OBS: n É O VALOR INFORMADO PELO USUÁRIO



def calcula_serie(numero):
    if numero <=0:
        return numero
    if numero == 1:
        print(numero+1)
        return numero+1
    resultado = (1 + numero**2)/numero
    print(resultado, end=' + ')
    return resultado + calcula_serie(numero-1)

def main():
    numero = int(input("Digite o valor final para a série a ser calculada: "))
    resultado_final = calcula_serie(numero)
    print("="*5, end='')
    print("RESULTADO FINAL", end='')
    print("="*5)
    print(resultado_final)


main()
