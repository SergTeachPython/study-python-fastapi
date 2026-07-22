# Рекурсія - коли функція викликає сама себе
# 1. Продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. Визначити умову виходу з рекурсії
# 3. Запустити рекурсію (виклик цієї функції)
#from lessons.lesson2 import result

#5! = 5 * 4 * 3 * 2 * 1
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсії
#     return number * factorial(number - 1)
#
# print(factorial(5))
#

# def fib(number):
#     if number == 0 or number == 1:
#         return number
#
#     return fib(number-1) + fib(number-2)
#
# print(fib(10))
#
# for i in range(10):
#     print(fib(i), end=' ')

# names = ["Alice", "Bob", "Charlie", "David"]
# ages = [25, 30, 22, 55]
# zipped_data = zip(names, ages)
# print(zipped_data)
# result = list(zipped_data)
# print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def is_even(num):
#     return num % 2 == 0
#
#
# result = []
# for num in numbers:
#     if is_even(num):
#         result.append(num)
#
# print(result)

# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)

# result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
# final_result = list(result)
# print(final_result)

import tkinter as tk

def show_info(name):
    print(f"hello, {name}!")

root = tk.Tk()
root.geometry("300x300")

button = tk.Button(root, text="Click Me", command=lambda: show_info("Vasya"))
button.pack()

root.mainloop()
