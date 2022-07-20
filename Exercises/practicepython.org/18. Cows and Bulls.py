import random

answer_list = []

while len(answer_list) < 4:
    answer_list.append(random.randint(0, 9))

user_input = int(input("Adivinhe um número de 4 dígitos: "))

