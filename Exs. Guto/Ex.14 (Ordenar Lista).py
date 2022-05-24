user_input = input("Digite uma lista de números: ")
user_list = user_input.split()
nums_list = [float(num) for num in user_list]

sorted_list = []

if len(nums_list) >= 2:
    while len(nums_list) > 0:
        min_num = min(nums_list)
        sorted_list.append(min_num)
        nums_list.remove(min_num)
    print(sorted_list)
else:
    print("Você precisa digitar uma lista de pelo menos 2 números!")
