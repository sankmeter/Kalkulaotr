number1 = int(input("Ввеідть значення "))
number2 = int(input("Введіть друге значення "))
operator3 = (input("Введіть знак "))
if number2 == 0 and operator3 == '/':
    print("Ділення на 0 неможлво")
elif operator3 == "+":
    summ = number1 + number2
    print(f'Сумма: {summ}')
elif operator3 == "/":
    div = number1 / number2
    print(f'Ділення: {div}')
elif operator3 == "-":
    sub = number1 - number2
    print(f'Різниця: {sub}')
elif operator3 == "*":
    mult = number1 * number2
    print(f'Множення: {mult}')







