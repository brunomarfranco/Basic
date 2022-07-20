import random

list_1 = []
list_2 = []

random_total_1 = random.randint(8, 13)
random_total_2 = random.randint(8, 13)

while len(list_1) < random_total_1:
    list_1.append(random.randint(0, 100))

while len(list_2) < random_total_2:
    list_2.append(random.randint(0, 100))

print(f'Lista 1: {list_1} \nLista 2: {list_2}')


overlap_list = []  # overlap_list = [num for num in set(list_1) if num in list_2]

for num in list_1:
    if num in list_2 and num not in overlap_list:
        overlap_list.append(num)


result = [str(num) for num in overlap_list]
result = ", ".join(result)

if len(overlap_list) == 0:
    print(f'Não existem números coincidentes entre as duas listas!')
elif len(overlap_list) == 1:
    print(f'O número que coincide em ambas as listas é o {result}.')
elif len(overlap_list) > 1:
    print(f'Os números que coincidem em ambas as listas são: {result}.')
