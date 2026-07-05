# letterA = chr(65)
# print(letterA)
# codeA =  ord("A")
# print(codeA)
#
# #text = "¼"
# text = "hello woRLD"
#
# # isalpha: повертає True, якщо рядок складається лише з алфавітних символів
# print(text.isalpha())   #поверне False
#
# # islower: повертає True, якщо рядок складається лише з малих літер (пробіли та цифри ігноруються)
# print(text.islower())
#
# # isupper: True, якщо усі символи великі літери (пробіли та цифри ігноруються)
# print(text.isupper())
#
# #isdigit: True, якщо усі символи - цифри
# print(text.isdigit())
#
# #isnumeric: True, якщо рядок є числом
# print(text.isnumeric())
#
# print(text.isdecimal())
#
# # startswith(str): True, якщо стрічка починається з підрядка str
# print(text.startswith('Hello'))
#
# # endswith(str): True, якщо стрічка закінчується на підрядок str
# print(text.endswith('D'))
#
# # lower() перекладає усі символи у нижній регістр
# # не змінює вихідну стрічку, а створює копію в нижньому регістрі
# result = text.lower()
# print(result)
# print(text)
#
# # upper(): перекладає усі символи у верхній регістр
# result = text.upper()
# print(result)
# print(text)
#
# # title(): перші літери усіх слів робить з великої літери (решту великих літер всередині слова переводить в нижній регістр)
# text = "qQQQQqqqqq wwwWWWwww qqwert"
# result = text.title()
# print(result)
# print(text)
#
# # capitalize(): перекладає у верхній регістр лише першу літеру першого слова рядка (решту великих літер всередині слова переводить в нижній регістр)
# print(text.capitalize())
#
# text = "    qertutrioe   "
# # rstrip() : видаляє пробіли справа (кінцеві)
# print(text.rstrip())
#
# # lstrip(): видаляє пробіли справа (початкові)
# print(text.lstrip())
#
# # strip(): видаляє справа і зліва (початкові і кінцеві)
# print(text.strip())
#
# text = "hello world"
# print(text)
#
# # ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# print(text.ljust(20))
#
# # ljust(width): якщо довжина рядка менша за параметр width, то ліворуч від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по правому краю
# print(text.rjust(20))
#
# # center(width) якщо довжина рядка менша за параметр width, то ліворуч і праворуч від рядка рівномірно
# # додаються пробіли, щоб доповнити значенння width, а сам рядок вирівнюється по центру
# print(text.center(20))

# find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
# text = "hello world"
# print(text.find("hello"))       #0
# print(text.find("l"))           #2
# print(text.rfind("l"))          #9
# #
# first_found_index = text.find("l")
# print(text.find("l", first_found_index) + 1)    #3
# #
# print(text.find("p"))

#######################
text = "hello world. goodbye world. hello world."
search_item = ". "

sentences = text.split(search_item)
print(sentences)

result = []
for sentence in sentences:
    result.append(sentence.capitalize())

print(result)

result_sentence = search_item.join(result)
print(result_sentence)
