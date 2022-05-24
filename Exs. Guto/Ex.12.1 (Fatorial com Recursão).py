num_input = int(input("Digite um número para calcular o seu fatorial: "))


def factorial(num):
    if num == 0:  # condição de parada (p/ recursão não loopar infinitamente)
        return 1
    result = factorial(num - 1)  # aqui começa o stack dos nums
    return num * result


if num_input >= 0:
    print(f'O fatorial de {num_input} é {factorial(num_input)}')
else:
    print("Digite um número inteiro e positivo!")
