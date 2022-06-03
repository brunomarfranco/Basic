user_input = int(input("Digite um número inteiro para dividir: "))

divisors_list = []

for num in range(1, user_input + 1):
    if user_input % num == 0:
        divisors_list.append(num)

print(divisors_list)
