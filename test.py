# Ex.13:

user_input = input("Digite pelo menos 3 números: ")
user_list = user_input.split()
nums_list = [int(num) for num in user_list]
total_nums = len(nums_list)

if total_nums >= 3:
    for index in range(total_nums):

        max_num = nums_list[index]

        for next_index in range(index + 1, total_nums):
            max_num = max(max_num, nums_list[next_index])
