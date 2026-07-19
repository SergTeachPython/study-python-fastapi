def popular_words (text, words):
    my_dict = {}
    my_dict = dict.fromkeys(words, 0)
    list_words = words
    text_to_check = text.lower()
    list_to_analys = text_to_check.split(" ")
    for word in list_words:
        if word in list_to_analys:
            my_dict[word] = text_to_check.count(word)
        else:
            my_dict[word] = 0
    return my_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
