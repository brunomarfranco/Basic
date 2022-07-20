num_input = int(input("Digite um número para calcular o seu fatorial: "))

factorial = 1

if num_input >= 0:
    for num in range(1, num_input + 1):
        factorial = factorial * num
    print(f'O fatorial de {num_input} é {factorial}')
else:
    print("Digite um número inteiro e positivo!")
