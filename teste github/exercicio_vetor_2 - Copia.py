# https://www.passeidireto.com/arquivo/56813560/listas-em-python-exercicios-iniciais

# Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
# Faça  a  função  "traduzir",  que  recebe  uma  lista  com  uma  mensagem   e  "traduz"  a  sequência armazenada de acordo com o código das amigas.
# DICA: crie uma string com as letras na ordem do código






def inicializa_vetor_codificadores():
    vetor_codificadores = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ]
    return vetor_codificadores





def inicializa_vetor_letras():
    vetor_letras = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return vetor_letras




def codificar(escolha, vetor_codificadores, vetor_letras):
    if escolha == 'C':
        mensagem = input('Digite a mensagem que será codificada: ')
        for palavra in mensagem:
            for letra in palavra:
                for i in range(0, len(vetor_codificadores)):
                    if letra == vetor_letras[i]:
                        print(vetor_codificadores[i], end='')





def decodificar(escolha, vetor_codificadores,vetor_letras):
    if escolha == 'D':
        palavra = ''
        while True:
            if escolha == 'D':
                mensagem = int(input('Digite a mensagem a ser decodificada: '))
                for i in range(0, len(vetor_letras)):
                    if mensagem == vetor_codificadores[i]:
                        print(vetor_letras[i])
                        palavra += vetor_letras[i]
                continar = input('Quer continuar(S/N)? ').upper()
                if continar == 'N':
                    break
        print('Resultado final: ', palavra)




def main():
    vetor_codificadores = inicializa_vetor_codificadores()
    vetor_letras = inicializa_vetor_letras()
    escolha = str(input('o que vc quer fazer: codificar ou decodificar uma mensagem(C/D)?')).upper()
    codificar(escolha, vetor_codificadores, vetor_letras)
    decodificar(escolha, vetor_codificadores, vetor_letras)



main()








