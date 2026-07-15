import string

def is_palindrome(text):
    only_alphabet = ""
    for char in text:
        if char in string.ascii_letters or char in string.digits:
            only_alphabet += char
    new_str = only_alphabet.lower()
    if new_str == new_str[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
