user_input = input("Digite os valores das colunas do histograma separados por um espaço: ")
user_list = user_input.split()
bars = []

for num in user_list:
    bars.append(int(num))

total_bars = len(bars)


def max_water(histogram_values, n):

    volume = 0

    for index in range(1, n - 1):

        max_left = histogram_values[index]

        for left_index in range(index):
            max_left = max(max_left, histogram_values[left_index])

        max_right = histogram_values[index]

        for right_index in range(index + 1, n):
            max_right = max(max_right, histogram_values[right_index])

        volume = volume + (min(max_left, max_right) - histogram_values[index])

    return volume


print(max_water(bars, total_bars))
