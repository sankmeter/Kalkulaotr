number1 = int(input("Ввеідть значення "))
number2 = int(input("Введіть друге значення "))
operator3 = (input("Введіть знак "))
if operator3 == "+":
    summ = number1 + number2
    print(f'Сумма: {summ}')
else:
    if operator3 == "/":
       div = number1 / number2
       print(f'Ділення: {div}')
    else:
       if operator3 == "-":
           sub = number1 - number2
           print(f'Різниця: {sub}')
       else:
           if operator3 == "*":
               mult = number1 * number2
               print(f'Множення: {mult}')




