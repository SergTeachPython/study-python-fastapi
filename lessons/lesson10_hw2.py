import string as st

def first_word(text):
    """ Пошук першого слова """
    for cur_symbol in st.punctuation:
        if cur_symbol != "'":
            text = text.replace(cur_symbol, ' ')
    text = text.lstrip()
    cur_list = text.split(' ')
    first_word = cur_list[0].strip()
    return first_word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
