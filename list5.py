my_list = [1,0,2,0,4]
my_list.sort(key=lambda x: (x == 0, x))
print(my_list)