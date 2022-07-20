user_input = int(input("Digite um número: "))

if user_input % 2 == 0:
    if user_input % 4 == 0:
        print(f'{user_input} é um número par e múltiplo de 4!')
    else:
        print(f'{user_input} é um número par!')
else:
    print(f'{user_input} é um número ímpar!')

num = int(input("Digite um número para ser dividido: "))
check = int(input("Digite um número para dividir: "))

if num % check == 0:
    print(f'{num} can be evenly divided by {check}!')
else:
    print(f'{num} cannot be evenly divided by {check}!')
