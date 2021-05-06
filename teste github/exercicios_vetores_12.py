#https://www.ime.usp.br/~macmulti/exercicios/vetores/index.html
#Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes.
# A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
#o cartão gabarito;
#o número de alunos da turma;
#o cartão de respostas para cada aluno, contendo o seu número e suas respostas.



def inicializa_gabarito():
    gabarito = []
    for i in range(0, 10):
        resposta_certa = input(f'Informe a {i+1}ª resposta certa: ').lower()
        gabarito.append(resposta_certa)
    return gabarito

def enfeita_codigo():
    print('=-'*30)

def inicializa_vetor_respostas(gabarito):
    vetor_respostas = [ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
    quantidade_alunos = int(input('Informe a quantidade de alunos: '))
    contador_acertos = 0
    contador_erros = 0
    for candidato in range(quantidade_alunos):
        enfeita_codigo()
        print(f"Candidato {candidato + 1}")
        enfeita_codigo()
        for resposta in range(10):
            resposta_aluno = input(f'Resposta {resposta+1} do candidato {candidato+1}: ').lower()
            vetor_respostas[resposta] = resposta_aluno
            if resposta_aluno in gabarito[resposta]:
                print('Resposta Certa')
                contador_acertos += 1
            else:
                print('Resposta errada')
                contador_erros += 1
        enfeita_codigo()
        print(f'Acertos candidato {candidato + 1}: ', contador_acertos)
        print(f'Erros candidato {candidato + 1}: ', contador_erros)
        contador_acertos = 0
        contador_erros = 0
    return vetor_respostas







def main():
    gabarito = inicializa_gabarito()
    vetor_respostas = inicializa_vetor_respostas(gabarito)
    enfeita_codigo()
    print('Gabarito: ', gabarito[:])


main()
