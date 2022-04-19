string_input = input("Digite uma lista de números separados por um espaço: ")
user_list = string_input.split()

for index in range(len(user_list)):
    user_list[index] = int(user_list[index])

print(user_list)

