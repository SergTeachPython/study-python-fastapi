import keyword
import string

is_variable = input("Please enter a string for checking: ")
answer =  True

for char in is_variable:
    if is_variable.index(char) == 0 and char.isdigit():
       answer = False

    if 65 <= ord(char) <= 90:
       answer = False

    if char in string.punctuation and char != "_":
        answer = False

if is_variable in keyword.kwlist:
    answer = False

if "__" in is_variable:
    answer = False

print(answer)
