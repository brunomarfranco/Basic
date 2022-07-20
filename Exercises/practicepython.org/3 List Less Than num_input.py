num_input = int(input("Digite um número inteiro: "))

nums_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for num in nums_list:
    if num < num_input:
        new_list.append(num)

print(new_list)
