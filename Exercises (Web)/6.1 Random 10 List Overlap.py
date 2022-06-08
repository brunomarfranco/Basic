import random

list_1 = []
list_2 = []

total_len = 0

while total_len < 10:
    list_1.append(random.randint(0, 100))
    list_2.append(random.randint(0, 100))
    total_len += 1

print(f'Lista 1: {list_1} \nLista 2: {list_2}')


overlap_set = set()

for num in list_1:
    if list_2.__contains__(num):
        overlap_set.add(num)


result = [str(num) for num in overlap_set]
result = ", ".join(result)

if len(overlap_set) == 0:
    print(f'Não existem números coincidentes entre as duas listas!')
elif len(overlap_set) == 1:
    print(f'O número que coincide em ambas as listas é o {result}.')
elif len(overlap_set) > 1:
    print(f'Os números que coincidem em ambas as listas são: {result}.')
