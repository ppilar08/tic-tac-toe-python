print('\n')
print('\033[36m=\033[m' * 40)
print(f'\n\033[36m{"Bem-vindos ao Jogo da Velha!":^40}\033[m\n')
print('\033[36m=\033[m' * 40)


print('\n\033[36mObjetivo:\033[m Seja o primeiro a formar uma linha com 3 símbolos iguais (X ou O), seja na horizontal, vertical ou diagonal.\n\033[36mOs jogadores se revezarão para escolher posições no tabuleiro.\033[m\n')
print('\033[36m-\033[m' * 50)


# While para o reinício do jogo.
while True: 
    tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    jogador_atual = 'X'
    jogadas = 0

    print(f'\n\033[34m{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print('-' * 9)
    print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print('-' * 9)
    print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\033[m')



# While da rodada.
    while True: 
        jogada = int(input(f'\n\033[30mJogador {jogador_atual}, escolha uma posição de 1 a 9 para jogar:\033[m '))



# While para verificar a jogada.
        while jogada < 1 or jogada > 9 or tabuleiro[jogada - 1] == 'X' or tabuleiro[jogada - 1] == 'O': 
            
            print('\n\033[31m❌ Jogada inválida.\033[m \033[30mTente novamente!\033[m')
            print(f'\n\033[34m{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
            print('-' * 9)
            print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
            print('-' * 9)
            print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\033[m')

            jogada = int(input(f'\n\033[30mJogador {jogador_atual}, escolha uma posição de 1 a 9 para jogar:\033[m '))

        tabuleiro[jogada - 1] = jogador_atual # Atribui a jogada do jogador da vez no tabueleiro.


    # Atualiza o tabuleiro depois da jogada do jogador
        print(f'\n\033[34m{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
        print('-' * 9)
        print(f'{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
        print('-' * 9)
        print(f'{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\033[m')


# verificação de vitória
        if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] or  # Verificação da linha 1
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] or # Verificação da liha 2
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] or # Verificação da linha 3
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] or # Verificação da coluna 1
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] or # Verificação da coluna 2
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] or # Verificação da coluna 3
            tabuleiro[6] == tabuleiro[4] == tabuleiro[2] or # Verificação da diagonal 1
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8]):  # Verificação da diagonal 2
            
            print(f'\n\033[32m✅ Vitória do jogador {jogador_atual}. PARABÉNS!\033[m')
            break


# Verificação de empate
        jogadas += 1
        if jogadas == 9:
            print('\n\033[33m🤝 O jogo empatou!\033[m')
            break


# Alternância de jogador
        if jogador_atual == 'X':
            jogador_atual = 'O'
        
        else:
            jogador_atual = 'X'



# Reinício do jogo.
    resposta = str(input('\n\033[30m🔄 Vamos jogar novamente? (S/N):\033[m ')).upper()

    while resposta not in ['N', 'S']: # Estrutura de repetição while para verificar se o jogador respondeu só S ou N.
        print('\n\033[31mResposta inválida.\033[m \033[30mPor favor digite só S ou N.\033[m')
        resposta = str(input('\n\033[30m🔄 Vamos jogar novamente? (S/N):\033[m ')).upper()

    if resposta == 'N':
        print('\n\033[30mObrigado por jogar.\033[m \033[31mEncerrando o programa...\033[m')
        break

    print('\n')