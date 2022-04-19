string_input = input("Digite uma lista de números separados por um espaço: ")
user_list = string_input.split()
nums_list = []

for num in user_list:
    nums_list.append(int(num))


if len(nums_list) >= 2:
    check_sum = False

    for index in range(len(nums_list)):
        for next_index in range(index+1, len(nums_list)):
            if nums_list[index] + nums_list[next_index] == nums_list[0]:
                print(f'{nums_list[index]} + {nums_list[next_index]} = {nums_list[0]}')
                check_sum = True

    if not check_sum:
        print(f"Não existem dois números nesta lista que somados resultem em {nums_list[0]}.")

else:
    print("Digite pelo menos 2 números!")
