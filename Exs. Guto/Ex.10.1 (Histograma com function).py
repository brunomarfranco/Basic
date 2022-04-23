user_input = input("Digite os valores das colunas do histograma separados por um espaço: ")
user_list = user_input.split()
bars = []

for num in user_list:
    bars.append(int(num))

total_bars = len(bars)


def max_water(bars, total_bars):

    volume = 0

    for index in range(1, total_bars - 1):

        left = bars[index]

        for left_index in range(index):
            left = max(left, bars[left_index])

        right = bars[index]

        for right_index in range(index + 1, total_bars):
            right = max(right, bars[right_index])

        volume = volume + (min(left, right) - bars[index])

    return volume


print(max_water(bars, total_bars))
