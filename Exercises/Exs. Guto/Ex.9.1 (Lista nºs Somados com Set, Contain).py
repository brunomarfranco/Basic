user_input = input("Digite uma lista de números separados por um espaço: ")
user_list = user_input.split()

nums_list = []

for num in user_list:
    nums_list.append(int(num))

if len(nums_list) >= 2:
    check_sum = False

    nums_set = set()
    for number in nums_list:
        if nums_set.__contains__(nums_list[0] - number):
            print(f'{number} + {nums_list[0] - number} = {nums_list[0]}')
            check_sum = True
        nums_set.add(number)

    if not check_sum:
        print(f"Não existem dois números nesta lista que somados resultem em {nums_list[0]}.")

else:
    print("Digite pelo menos 2 números!")
