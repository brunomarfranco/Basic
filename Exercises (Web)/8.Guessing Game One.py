import random

drawn_num = random.randint(1, 9)

guess_count = 0
end_game = False


while not end_game:
    guess = input("Digite um número de 1 a 9 para adivinhar: ").lower()

    if guess == "exit":
        break
    else:
        guess = int(guess)
        guess_count += 1

    if guess == drawn_num:
        if guess_count > 1:
            print(f'Você acertou, o número era {drawn_num}! Você tentou {guess_count} vezes.')
        else:
            print(f'Você acertou, o número era {drawn_num}! Você tentou 1 vez.')
    elif guess > drawn_num:
        print("Tente um número menor!")
        continue
    elif guess < drawn_num:
        print("Tente um número maior!")
        continue


    new_game = input("Quer jogar de novo? Digite 'sim' ou 'não': ").lower()

    if new_game == "não":
        print("Até a próxima!")
        end_game = True
    elif new_game == "sim":
        print("Vamos lá!")
        drawn_num = random.randint(1, 9)
        guess_count = 0
