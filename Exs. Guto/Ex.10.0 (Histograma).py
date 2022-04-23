user_input = input("Digite os valores das colunas do histograma separados por um espaço: ")
user_list = user_input.split()
bars = []

for num in user_list:
    bars.append(int(num))

total_bars = len(bars)

volume = 0

for index in range(1, total_bars - 1):

    left = bars[index]

    for left_index in range(index):
        left = max(left, bars[left_index])

    right = bars[index]

    for right_index in range(index + 1, total_bars):
        right = max(right, bars[right_index])

    volume = volume + (min(left, right) - bars[index])

print(volume)


# range (1, total_bars - 1): primeira e última coluna não podem armazenar água, pois não estão entre colunas

# ver qual é a maior coluna à esquerda e qual a maior à direita:
# left/right bars[index] garantem que o maior nº considerado não seja menor do que a coluna da vez
# range (index) itera todas as colunas à esquerda da index (sem incluí-la)
# left/right é a maior coluna à esquerda/direita. Vai comparar o máx valor registrado anteriormente c/ a iteração da vez
# range(index + 1, total_bars) itera todas as colunas à direita da index (sem incluí-la)

# min(left, right) é a capacidade máx. em unidades que as barragens permitem a coluna da vez chegar
# - bars[index] subtrai da capacidade máx de altura, o valor em unidades da "estrutura" da coluna
# volume é a quantidade total de água que as colunas anteriores conseguiram armazenar,
# somada à quantidade que a coluna da vez consegue armazenar
