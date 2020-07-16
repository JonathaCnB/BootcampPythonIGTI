from random import choice
from lib import *
from time import sleep
escolha = str(selecaoPalavra().strip())  # Recebe uma palavra aleatoria de uma lista na lib
totJogadas = 6  # Contador de tentativas
contVitorias = contDerrotas = 0
letrasUsadas = []
letrasCertas = []
lstPalavra = []
plural = ['tentativas', 'vezes', 'tentativa', 'vez']
acertou = False

###### INICIO DO JOGO ######
while True:
    for l in range(0, len(escolha)):
        lstPalavra.append('- ')
        print(f'\033[1;30m- \033[m', end='')

    while acertou is False:
        if totJogadas > 1:
            selPlural = plural[0]
        else:
            selPlural = plural[2]
        print(f'\n\033[1;30mA palavra tem {len(escolha)} letras, restão {totJogadas} {selPlural}\033[m')
        chute = verificaString(f'\n{"Digite uma letra: "}')  # Recebe o chute e testa se é string
        print('\033[1;33mVerificando...\033[m')
        sleep(1)
        if chute in letrasUsadas:
            print(f'\033[7;30m{chute}: Já foi usada, por favor escolha outra!\033[m')

        elif chute not in escolha:  # Se não fizer parte aparecera a mensagem abaixo e subtrai 1 do total de chutes
            print(f'\033[1;30m{chute}\033[m: \033[1;31mNão está na palavra sorteada!\033[m')
            letrasUsadas.append(chute)
            totJogadas -= 1

        else:   # Verifica se a letra está na palavra escolhida
            for i in range(0, len(escolha)):  # Laço caso a letra esteja certa!
                if chute == escolha[i]:
                    lstPalavra[i] = chute
                    letrasUsadas.append(chute)
                    letrasCertas.append(chute)

        if totJogadas == 0:
            print(f'\033[7;31mGame Over!\033[m\033[1;31m {escolha}\033[1;31m: Era a palavra correta!\033[m')
            contDerrotas += 1
            break
        for p in lstPalavra:
            print(f'\033[1;30m{p}', end=' ')

        if len(letrasCertas) == len(escolha):  # Finalização!
            print('\033[7;30mAcertou, Parabens!\033[m')
            contVitorias += 1
            acertou = True
    resp = ' '
    resp = str(input("Deseja Jogar novamente? [S/N] ")).strip().upper()[0]
    if resp not in 'S':
        totPartidas = contVitorias + contDerrotas
        if totPartidas > 1:
            sel = plural[1]
        else:
            sel = plural[3]

            print(f'\033[1;34mJogamos {contDerrotas + contVitorias} {sel}, você ganhou {contVitorias} !!!\033[m')

        print(f'\033[7;34m{"VOLTE SEMPRE!":^35}\033[m')
        break
    else:
        escolha = str(selecaoPalavra().strip())
        totJogadas = 6
        acertou = False
        letrasUsadas.clear()
        letrasCertas.clear()
        lstPalavra.clear()
