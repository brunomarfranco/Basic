num_input = int(input("Digite um número para descobrir se é um número primo: "))


def prime(number):
    divisors_list = []

    for num in range(1, number + 1):
        if number % num == 0:
            divisors_list.append(num)

    if len(divisors_list) == 2:
        print(f'O número {number} é primo!')
    else:
        print(f'O número {number} não é primo!')


prime(num_input)
