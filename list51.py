my_list = [0, 2, 3, 4, 5, 8]
result = 0
for i in range(0, len(my_list ), 2):
    result += my_list[i]
if my_list:
    result = result * my_list[-1]
print(result)