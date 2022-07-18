import random

nums_list = []
nums_list_total = random.randint(7, 13)

while len(nums_list) < nums_list_total:
    nums_list.append(random.randint(0, 100))

print(f'A lista randomizada é: {sorted(nums_list)}')


def remove_duplicates(numbers_list):
    new_set = set()

    for num in numbers_list:
        new_set.add(num)

    return sorted(new_set)


print(remove_duplicates(nums_list))
