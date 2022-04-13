print("WHILE LOOP")

i = 1
while i <= 10:
    print(i)
    i += 1  # i = i + 1

print("Done with loop")

print("\n")


print("FOR LOOP")

for letter in "Giraffe Academy":
    print(letter)

friends = ["Gil", "Ian", "Caio"]
for friend in friends:
    print(friend)

for number in range(10):  # 0-9. Pode usar "," pra delimitar entre um nº e outro
    print(number)

for index in range(len(friends)):   # variável index passa a ter o valor de 0, depois 1, depois 2
    print(friends[index])           # friends[0], friends [1], friends [2]

for index in range(10):
    if index == 0:
        print("First iteration")
    elif 0 < index < 5:
        print(f'{index} is your floor number')
    elif 5 <= index < 9:
        print(f'{index} is your ceil number')
    elif index == 9:
        print("Last iteration")


print("EXPONENT FUNCTION")


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num      # result depois do "=" é a variável da iteração anterior!
    return result


print(raise_to_power(2, 3))
