import string


all_letters = string.ascii_letters
char_range = input("Input a range in a-z format: ")
start_index = all_letters.find(char_range[0])
end_index = all_letters.find(char_range[-1:])
word = all_letters[start_index:end_index+1]
print(word)


