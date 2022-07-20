user_input = input("Digite pelo menos 3 números diferentes: ")
user_list = user_input.split()
nums_list = [float(num) for num in user_list]


def third_largest(list_of_numbers):
    max_number = 0
    second_max_number = 0
    third_max_number = 0

    for number in list_of_numbers:
        if number > max_number:
            max_number, second_max_number, third_max_number = number, max_number, second_max_number
        elif number > second_max_number and number != max_number:
            second_max_number, third_max_number = number, second_max_number
        elif number > third_max_number and max_number != number != second_max_number:
            third_max_number = number
    return third_max_number


if len(nums_list) >= 3:
    print(f'O 3º maior número é {third_largest(nums_list)}')
else:
    print("Você precisa digitar ao menos 3 números diferentes!")
