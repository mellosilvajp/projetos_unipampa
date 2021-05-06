#http://200.17.137.109:8081/novobsi/Members/cicerog/disciplinas/introducao-a-programacao/arquivos-2015-2/07%20python%20-%20listas.pdf

#Faça um programa que receba a temperatura média
#de cada mês do ano e armazene-as em uma lista.
#Em seguida, calcule a média anual das temperaturas
#e mostre a média calculada juntamente com todas as
#temperaturas acima da média anual, e em que mês
#elas ocorreram (mostrar o mês por extenso: 1 –
#Janeiro, 2 – Fevereiro, . . . ).

def enfeita_codigo():
    print('=-'*30)

def calcula_media_anual(lista_temperaturas):
    soma = 0
    for i in range(0, len(lista_temperaturas)):
        soma += lista_temperaturas[i]
    media_anual = int(soma / 12)
    return media_anual

def mostra_meses_acima_da_media():
    for i in range(0, len(lista_temperaturas)):
        if lista_temperaturas[i] > media_anual:
            print(lista_meses[i], '-', lista_temperaturas[i])
            meses_acima_da_media.append(lista_meses[i])


lista_temperaturas = [32, 32, 33, 32, 27, 27, 26, 27, 25, 30, 30, 31]
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
meses_acima_da_media = []
soma = 0
for i in range(0, len(lista_temperaturas)):
    soma += lista_temperaturas[i]
media_anual = int(soma / 12)
print('Média anual:', media_anual)
enfeita_codigo()
print('Meses acima da média: ')
enfeita_codigo()
for i in range(0, len(lista_temperaturas)):
    if lista_temperaturas[i] > media_anual:
        print(lista_meses[i], '-', lista_temperaturas[i])
        meses_acima_da_media.append(lista_meses[i])
print('Média anual: ', media_anual)
enfeita_codigo()
print('Temperatura média de cada mês:')
enfeita_codigo()
for i in range(0,len(lista_meses)):
    print(lista_meses[i], '-', lista_temperaturas[i])
