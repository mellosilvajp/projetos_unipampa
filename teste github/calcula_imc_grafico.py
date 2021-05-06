import re
import PySimpleGUI as sg
import random

def verifica_dados(sexo, idade, altura, peso, atividade):
    if sexo == "" or (sexo[0] != 'm' and sexo[0] != 'f'):
        return "sexo invalido! opcoes validas são m ou f"

    if idade.isdigit() == False:
        return "nao eh um numero inteiro positivo"

    idade = int(idade)
    if idade <= 0 or idade > 130:
        return "idade invalida. intervalo valido de 1 a 130"

    if re.match(r'^\d+(?:\.\d+)$', altura) is None:
        return "altura deve ser um numero real e positivo"

    if re.match(r'^\d+(?:\.\d+)$', peso) is None:
        return "peso deve ser um numero real e positivo"

    if atividade == "" or (atividade[0] != 's' and atividade[0] != 'm' and atividade[0] != 'i'):
        return "atividade invalida. opcoes validas são s, m ou i"

    return None

def calcula_imc(altura, peso):
    imc = float(peso) / (float(altura) * float(altura))
    mensagem = "None"
    if imc < 18.5:
        mensagem = "Abaixo do peso"
    elif imc <= 24.9:
        mensagem = "Peso normal"
    elif imc <= 29.9:
        mensagem = "Sobrepeso"
    elif imc <= 34.9:
        mensagem = "Obesidade grau 1"
    elif imc <= 39.9:
        mensagem = "Obesidade grau 2"
    else:
        mensagem = "Obesidade grau 3"
    return imc, mensagem

def inicia_layout():
    # Define the window's contents
    layout = [[sg.Text("Informe o sexo (m ou f):")],
              [sg.Input(key='-SEXO-')],
              [sg.Text("Informe a idade:")],
              [sg.Input(key='-IDADE-')],
              [sg.Text("Informe o valor da altura:")],
              [sg.Input(key='-ALTURA-')],
              [sg.Text("Informe o peso:")],
              [sg.Input(key='-PESO-')],
              [sg.Text("Atividade fisica (s, m, i):")],
              [sg.Input(key='-ATIVIDADE-')],
              [sg.Text(size=(55,3), key='-SAIDA-')],
              [sg.Button('Ok'), sg.Button('Sair'), sg.Button('Limpar'), sg.Button('Mensagem do dia')]]
    return layout

def mensagem_do_dia(window):
    mensagemdia = random.randint(1, 10)
    if mensagemdia == 1:
        window.FindElement('-SAIDA-').Update('O poder está dentro de você, na sua mente,'
                                             ' pois se acreditar que consegue não haverá obstáculo capaz '
                                             'de impedir o seu sucesso.')
    if mensagemdia == 2:
        window.FindElement('-SAIDA-').Update('Se ao enfrentar os problemas da vida lhe parecer'
                                             ' que está escalando uma montanha impossível, lembre-se'
                                             ' que a paisagem que avistará no topo compensará qualquer esforço seu.')
    if mensagemdia == 3:
        window.FindElement('-SAIDA-').Update('A vida tanto lhe pode dar o melhor como o pior,'
                                             ' mas é você quem escolhe aquilo que vai permanecer'
                                             ' ou ficar para trás.')
    if mensagemdia == 4:
        window.FindElement('-SAIDA-').Update('Nunca é tarde demais para ser aquilo que sempre desejou ser.')
    if mensagemdia == 5:
        window.FindElement('-SAIDA-').Update('Teste os seus limites, enfrente os seus medos e não deixe que nada'
                                             ' impeça você de pelo menos tentar!')
    if mensagemdia == 6:
        window.FindElement('-SAIDA-').Update('Você é mais forte e mais capaz do que imagina, e a conquista dos seus'
                                             ' objetivos depende apenas de você!')
    if mensagemdia == 7:
        window.FindElement('-SAIDA-').Update('Sempre que algo falhar, batalhe ainda mais forte até encontrar'
                                             ' empenho novamente!')
    if mensagemdia == 8:
        window.FindElement('-SAIDA-').Update('A melhor maneira de melhorar o padrão de vida está em'
                                             ' melhorar o padrão de pensamento.')
    if mensagemdia == 9:
        window.FindElement('-SAIDA-').Update('Não desista já, pois o caminho que leva ao sucesso '
                                             'tem várias etapas e inclui alguns obstáculos!')
    if mensagemdia == 10:
        window.FindElement('-SAIDA-').Update('Lutar com todas as forças por um objetivo não significa vencer'
                                             ' sempre, mas é a garantia que no final estaremos de consciência tranquila.')

def limpar_campos_da_janela(window):
    window.FindElement('-SEXO-').Update('')
    window.FindElement('-IDADE-').Update('')
    window.FindElement('-ALTURA-').Update('')
    window.FindElement('-PESO-').Update('')
    window.FindElement('-ATIVIDADE-').Update('')
    window.FindElement('-SAIDA-').Update('')

def main():
    # Create the window
    window = sg.Window('Calculadora de IMC', inicia_layout())

    # Display and interact with the Window using an Event Loop
    while True:
        evento, valores = window.read()
        # See if user wants to quit or window was closed
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            break

        if evento == 'Limpar':
            limpar_campos_da_janela(window)
            continue
        if evento == 'Mensagem do dia':
            mensagem_do_dia(window)
            continue



        # executa botao Ok
        mensagem = verifica_dados( valores['-SEXO-'],
                                   valores['-IDADE-'],
                                   valores['-ALTURA-'],
                                   valores['-PESO-'],
                                   valores['-ATIVIDADE-'])

        imc = 0
        if mensagem == None:
            imc, mensagem = calcula_imc(valores['-ALTURA-'],valores['-PESO-'])

        # Output a message to the window
        window['-SAIDA-'].update('IMC: ' + "{:.2f}".format(imc) + ' MSG: ' + mensagem)

    # Finish up by removing from the screen
    window.close()

main()
