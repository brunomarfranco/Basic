list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap_set = set()

for num in list_1:
    if list_2.__contains__(num):
        overlap_set.add(num)

print(overlap_set)

# print({num for num in list_1 if list_2.__contains__(num)})
