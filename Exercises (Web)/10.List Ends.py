nums_list = [5, 10, 15, 20, 25]


def list_ends(original_list):

    new_list = [original_list[0], original_list[-1]]
    return new_list


print(list_ends(nums_list))
