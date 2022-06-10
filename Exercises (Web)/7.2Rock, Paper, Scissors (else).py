player_1 = input("Digite o nome do 1º jogador: ").capitalize()
player_2 = input("Digite o nome do 2º jogador: ").capitalize()

end_game = False

while not end_game:

    P1_turn = input(f'{player_1}: Pedra, papel ou tesoura? ').lower()
    P2_turn = input(f'{player_2}: Pedra, papel ou tesoura? ').lower()

    if P1_turn == P2_turn:
        print("Empate, ninguém venceu!")
        continue

    elif P1_turn == "pedra":
        if P2_turn == "tesoura":
            print(f'Parabéns {player_1}, você venceu!')
        else:
            print(f'Parabéns {player_2}, você venceu!')

    elif P1_turn == "papel":
        if P2_turn == "pedra":
            print(f'Parabéns {player_1}, você venceu!')
            else:
            print(f'Parabéns {player_2}, você venceu!')

    elif P1_turn == "tesoura":
        if P2_turn == "papel":
            print(f'Parabéns {player_1}, você venceu!')
            else:
            print(f'Parabéns {player_2}, você venceu!')

    else:
        print("Digite corretamente a arma de sua escolha!")

    new_game = input('Querem jogar de novo? Responda "sim" ou "não": ').lower()

    if new_game == "sim":
        print("Vamos lá!")
    elif new_game == "não":
        end_game = True
