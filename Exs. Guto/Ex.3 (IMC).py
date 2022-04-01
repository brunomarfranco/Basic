height = float(input("Digite sua altura em metros: "))
weight = float(input("Digite seu peso em kg: "))
IMC = weight / height**2

# if IMC < 18.5:
#     print("Você está abaixo do peso ideal.")
# elif IMC < 25:
#     print("Parabéns! Você está no peso ideal!")
# elif IMC < 30:
#     print("Você está com sobrepeso.")
# elif IMC < 35:
#     print("Você está com obesidade grau I.")
# elif IMC < 40:
#     print("Você está com obesidade severa grau II.")
# else:
#     print("Você está com obesidade mórbida grau III.")

if IMC > 18.5 and IMC < 25:
    print("Parabéns! Você está no peso ideal!")