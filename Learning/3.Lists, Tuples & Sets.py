print("LISTS")

friends = ["Gil", "Ian", "Guilherme", "Gil", "Bernardo", "Sérgio"]
print(friends[1:3])
print(friends[1:])
print(friends[:3])
print(friends[1:-1:2])  # começo:fim:steps
print(friends[:-1:2])
print(friends[::-1])  # reverse
friends[-2] = "Caio"
print(friends[0] + " and " + friends[-2] + " are my closest friends")

friends.append("Josimar")
print(friends)
friends.insert(-1, "Karen")  # -x na verdade se traduz p/ len(list) - x; insert coloca o novo elemento no index pedido
print(friends)               # e empurra p/ direita o elemento que estava nessa posição anteriormente
friends.remove("Josimar")
print(friends)
friends.pop()
print(friends)
print(friends.index("Guilherme"))
print(friends.count("Gil"))
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)

lucky_numbers = [13, 5, 7, 11, 49]
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
print(friends + lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
friends.clear()
print(friends)

if lucky_numbers.__contains__(7):
    print("True, it contains 7")


# Split & Join
my_name = "Bruno Martins Franco"
all_names = my_name.split()  # splita a string em itens a partir de um separador pré-definido (separator, maxsplit)
print(all_names)
my_friends = " ".join(friends)  # junta os itens de uma lista em uma string, adicionando um separador str entre eles
print(my_friends)

nums_list = input("Digite uma lista de números: ")           # nums_list = "1 2 3 4"
nums_list1 = input("Digite uma lista de números: ").split()  # nums_list = ["1", "2", "3", "4"]
nums_list2 = [input("Digite uma lista de números: ")]        # nums_list = ["1 2 3 4"]

# List Comprehension
user_list = input("Digite uma lista de números: ").split()
new_list = [int(num) for num in user_list]  # retorna "num" manipulado com int para cada "num" que houver em "user_list"
print("\n")


print("TUPLES")

coordinates = (4, 5)
print(coordinates[-1])

coordinates = [(4, 5), (6, 7), (50, 55)]
print(coordinates[2])
print("\n")


print("SETS")

nums_set = {5, 4, 3, 1, 0, 2}
print(nums_set)

groceries = set()
groceries.add("apple")
print(groceries)
