user_input = input("Digite uma lista de números: ")
user_list = user_input.split()

nums_list = [int(num) for num in user_list]
even_squared = [num ** 2 for num in nums_list if num % 2 == 0]

print(even_squared)
