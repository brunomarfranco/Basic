user_input = input("Digite uma lista de números: ")
user_list = user_input.split()
nums_list = [float(num) for num in user_list]

sorted_list = []

if len(nums_list) >= 2:
    for index in range(len(nums_list)):
        max_num = max(nums_list)
        sorted_list.insert(- index, max_num)
        nums_list.remove(max_num)
    print(sorted_list)
else:
    print("Você precisa digitar uma lista de pelo menos 2 números!")


# -x na verdade se traduz p/ len(list) - x
# insert coloca o novo elemento no index pedido e empurra p/ direita o elemento que estava nessa posição anteriormente
