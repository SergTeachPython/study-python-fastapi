from unittest import result
#
# numb = int(input("Enter a integer number: "))
# while numb > 9:
#     length = len(str(numb)) - 1
#     result = 1
#     for i in range(length, 0 , -1):
#         one_digit = numb // pow(10, i)
#         numb %= pow(10, i)
#         result *= one_digit
#     numb = result * numb
# print(numb)

# #Legacy ver.1
# number = int(input("Enter your number: "))
#
# while number > 9:
#     result = 1
#     while number > 0:
#         num = number % 10
#         number = number // 10
#         result = result * num
#     number = result
# print(result)

# #Legacy ver.2
#
# number = 729
# print(number)
#
# while number > 9:
#     temp_number = str(number)
#     number = 1
#     for char in temp_number:
#         if char.isdigit():
#             number *= int(char)
#     print(number)
