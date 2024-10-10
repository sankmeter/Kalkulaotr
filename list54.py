
my_string = input("Please enter your variable:")
result = False
if my_string.isidentifier():
    if my_string == "_" or my_string.islower():
        result = True
print(result)

