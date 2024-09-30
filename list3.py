def split_list(lst):
    if not lst:
        return [[],[]]
    middle_index = (len(lst) + 1) // 2
    first_part = lst[:middle_index]
    second_part = lst[middle_index:]
    return [first_part, second_part]
my_list = [1, 2, 3, 4, 5]
result = split_list(my_list)
print(result)
