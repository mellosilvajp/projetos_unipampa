#o programa consulta o vetor de palavras e mostra quantas vogais tem em cada uma.



palavras = [ 'computador', 'processador', 'memoria', 'placa', 'programa', 'cooler', 'fonte', 'gabinete', 'disco' ]

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()}, temos as vogais: ', end='   ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='   ')
