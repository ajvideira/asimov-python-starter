import random

moves = ['Pedra', 'Papel', 'Tesoura']

rules = {
    0: 2,
    1: 0,
    2: 1
}

score = [0,0,0]

def print_score():
    print('\nPLACAR')
    print(f'Jogador: {score[0]}')
    print(f'Computador: {score[1]}')
    print(f'Empate: {score[2]}')

def read_player_move():
    while True:
        move = input('Escolha sua jogada (Pedra: 0, Papel: 1 ou Tesoura: 2): ')
        if move == '0' or move == '1' or move == '2':
            return int(move)
        else:
            print('Movimento inválido!')

def main():
    print('-----------------------------------')
    print('-- PEDRA, PAPEL OU TESOURA v1.0  --')
    print('-----------------------------------')

    while True:
        print_score()

        player_choice = read_player_move()

        print(f'Jogador 1 escolheu: {moves[player_choice]}')

        computer_choice = random.randint(0, 2)

        print(f'Computador escolheu: {moves[computer_choice]}')

        if player_choice == computer_choice:
            print('Empate!')
            score[2] += 1
        elif rules[player_choice] == computer_choice:
            print('Vitória do jogador 1!')
            score[0] += 1
        else:
            print('Vitória da máquina')
            score[1] += 1

        play_again = input('\nDeseja jogar novamente? (S/N): ')

        if play_again.upper() != 'S':
            break

if __name__ == "__main__":
    main()