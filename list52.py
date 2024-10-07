from tracemalloc import take_snapshot

my_list = [1, 2, 3, 4, 5, 6, 7, 9]
print("Old list", my_list)
new_list1 = my_list[0]
new_list2 = my_list[2]
new_list3 = my_list[-2]
new_list = [new_list1,  new_list2, new_list3]
print("New list", new_list)