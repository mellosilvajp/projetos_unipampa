# https://www.passeidireto.com/arquivo/56813560/listas-em-python-exercicios-iniciais
#
# Os alunos de uma turma foram muito mal em uma prova.
# O professor resolveu, então considerar a maior nota como o 10.0 e transformar as demais notas em relação
# a esta nota da seguinte maneira:  nota do aluno * 10/ maior nota.
# Faça uma função que receba a lista de notas dos alunos, calcule  a nova nota dos
# alunos mostrando as notas antigas e as novas na tela.



def inicializa_notas_originais(melhor_nota):
    notas_originais = []
    notas_originais.append(melhor_nota)
    return notas_originais

def inicializa_notas_novas():
    novas_notas = []
    novas_notas.append(10)
    return novas_notas



def enfeita_codigo():
    print('='*30)


def adiciona_valores_aos_vetores(notas_originais, novas_notas, melhor_nota):
    quantidade_alunos = int(input('Digite a quantidade de alunos: '))
    enfeita_codigo()
    for i in range(0, quantidade_alunos):
        notas_alunos = int(input('Digite a nota dos demais alunos: '))
        notas_originais.append(notas_alunos)
        nota_nova = int(notas_alunos*10/melhor_nota)
        print('A nova nota deste aluno é: ', nota_nova)
        novas_notas.append(nota_nova)
        enfeita_codigo()




def main():
    melhor_nota = int(input('Qual foi a melhor nota da turma(entre 0 a 10)? '))
    novas_notas = inicializa_notas_novas()
    notas_originais = inicializa_notas_originais(melhor_nota)
    adiciona_valores_aos_vetores(notas_originais, novas_notas, melhor_nota)
    enfeita_codigo()
    print('A melhor nota foi: ', melhor_nota)
    print('As notas originais eram: ', sorted(notas_originais[:]))
    print('As novas notas são: ', sorted(novas_notas[:]))



main()
