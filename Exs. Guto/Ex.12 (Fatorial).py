num_input = int(input("Digite um número para calcular o seu fatorial: "))
nums_list = [num_input]

factorial = 1

if num_input >= 0:
    for num in nums_list:
        if num > 1:
            nums_list.append(num - 1)
            factorial = factorial * num
    print(f'O fatorial de {num_input} é {factorial}')
else:
    print("Digite um número inteiro e positivo!")
