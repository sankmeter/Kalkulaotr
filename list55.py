import string
from string import punctuation

input_letters = input("Enter 2 symbols using a hyphen: ").strip()
start_letter, end_letter = input_letters.split('-')
start_letter = start_letter.strip()
end_letter = end_letter.strip()
letters = string.ascii_letters
start_index =  letters.index(start_letter)
end_index = letters.index(end_letter)
if start_index  <= end_index:
    selected_letters = letters[start_index:end_index + 1]
else:
    if end_index == 0:
        selected_letters = letters[start_index::-1]
    else:
        selected_letters = letters[start_index:end_index - 1:-1]
print( "symbols between", start_letter,"and", end_letter, "Inclusive:", ", ".join(selected_letters))