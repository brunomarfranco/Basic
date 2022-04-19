string_input = input("Digite uma lista de números separados por um espaço: ")
user_list = string_input.split()

nums_list = [int(num) for num in user_list]

print(nums_list)
