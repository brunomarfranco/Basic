user_input = input("Digite pelo menos 3 números: ")
user_list = user_input.split()
nums_list = [float(num) for num in user_list]

if len(nums_list) >= 3:
    max_num = max(nums_list)
    nums_list.remove(max_num)
    second_max_num = max(nums_list)
    nums_list.remove(second_max_num)
    third_max_num = max(nums_list)
    print(third_max_num)
else:
    print("Você precisa digitar ao menos 3 números!")
