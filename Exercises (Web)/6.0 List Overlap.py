list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap_list = []

for num in list_1:
    if num in list_2 and num not in overlap_list:
        overlap_list.append(num)

print(overlap_list)

# Como gerar random lists?
