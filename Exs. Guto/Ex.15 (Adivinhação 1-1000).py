input("Pense em um número inteiro entre 1 e 1000 e aperte Enter para começar! ")

right_guess = False
tries_count = 0
min_value = 1
max_value = 1000

while not right_guess:
    half_value = (min_value + max_value) // 2
    win_question = input(f'{half_value} é o número que você pensou? ').lower()
    tries_count += 1

    if win_question == "sim":
        right_guess = True
    elif win_question == "não":
        funnel_question = input(f'O número que você pensou é maior ou menor que {half_value}? ').lower()

        if funnel_question == "maior":
            min_value = half_value + 1
        elif funnel_question == "menor":
            max_value = half_value - 1


print(f'Foram necessárias {tries_count} tentativas.')

# busca binária
# akinator.com
