user_input = int(input("Digite quantos números da sequência Fibonacci você quer gerar: "))


def fibonacci_sequence(number):
    fib_nums = [0, 1]

    if number == 1:
        return fib_nums[0]

    elif number > 1:
        for index in range(number - 2):  # pois já há 2 nºs pré-definidos na lista
            fib_nums.append(fib_nums[index] + fib_nums[index + 1])
        return fib_nums

    else:
        print("Você precisa gerar pelo menos um número!")


print(fibonacci_sequence(user_input))
