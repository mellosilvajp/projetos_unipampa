#http://200.17.137.109:8081/novobsi/Members/cicerog/disciplinas/introducao-a-programacao/arquivos-2015-2/07%20python%20-%20listas.pdf

#Utilizando listas faça um programa que faça 5 perguntas para uma
#pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# “Tinha dívidas com a vítima?"
# "Já trabalhou com a vítima?“
# O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como
# "Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def faz_perguntas(lista_de_perguntas):
    confirmacoes = 0
    for i in range(0, len(lista_de_perguntas)):
        print('Responda com S (sim) ou N (não)')
        resposta = input(lista_de_perguntas[i]).upper()
        if resposta == 'S':
            confirmacoes += 1
    return confirmacoes

def verifica_reu(confirmacoes):
    if confirmacoes == 5:
        print('Assassino!')
    elif confirmacoes > 2 and confirmacoes < 5:
        print('Cúmplice!')
    elif confirmacoes == 2:
        print('Suspeito!')
    else:
        print('Inocente!')

def main():

    lista_de_perguntas =[ "Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
                     "Tinha dívidas com a vítima?",  "Já trabalhou com a vítima?"]

    confirmacoes = faz_perguntas(lista_de_perguntas)

    verifica_reu(confirmacoes)


main()
