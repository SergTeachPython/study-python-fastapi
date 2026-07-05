import string

start_str = input("Please enter a string for conversion: ")
end_str = "#"

new_str = start_str.title()

len_str = len(new_str)
if len_str > 139:
    len_str = 139

for i in range(len_str):
    if i == 0 and new_str[i].isalpha():
        end_str += new_str[i].capitalize()

    elif new_str[i] in string.punctuation or ord(new_str[i]) == 32:
        #miss char
        end_str = end_str

    else:
        end_str += new_str[i]

print(end_str)
