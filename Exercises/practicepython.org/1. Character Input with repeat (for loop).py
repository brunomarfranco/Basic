name = input("Digite o seu nome: ").capitalize()
age = int(input("Digite sua idade: "))
repeat_input = int(input("Digite quantas vezes você quer receber a mensagem: "))

hundred_years = 2022 + (100 - age)

for num in range(0, repeat_input):
    print(f'{name}, você terá 100 anos no ano de {hundred_years}')


