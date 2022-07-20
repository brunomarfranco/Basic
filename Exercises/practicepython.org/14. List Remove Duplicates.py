import random

nums_list = []
nums_list_total = random.randint(7, 13)

while len(nums_list) < nums_list_total:
    nums_list.append(random.randint(0, 100))

print(f'A lista randomizada é: {sorted(nums_list)}')


def remove_duplicates(numbers_list):
    new_list = []

    for num in numbers_list:
        if num not in new_list:
            new_list.append(num)

    return sorted(new_list)


print(remove_duplicates(nums_list))
