name = input("Digite o seu nome: ").capitalize()
age = int(input("Digite sua idade: "))
repeat_input = int(input("Digite quantas vezes você quer receber a mensagem: "))

hundred_years = 2022 + (100 - age)

print(repeat_input * f'{name}, você terá 100 anos no ano de {hundred_years}. \n')
