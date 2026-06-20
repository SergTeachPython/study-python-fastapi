#2.1. Square of number
number = input("Enter a number: ")
square_of_number = int(number)**2
print("Квадрат значення:", square_of_number)

#2.2. Average of three numbers
number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))
average_value = (number1 + number2 + number3) / 3
print("Середнє значення:", average_value)

#2.3. Minutes in hours and minutes
minutes = int(input("Enter a minutes: "))
hours = minutes // 60
minutes_60 = minutes % 60
print(hours, "годин", minutes_60, "хвилин")

#2.4. Calculate discount
price = int(input("Enter a price: "))
discount = int(input("Enter a discount: "))
price_with_discount = price - price * discount / 100
print("Ціна зі знижкою:", price_with_discount)

#2.5. Last digit of number
number_last_digit = int(input("Enter a number: "))
last_digit = number_last_digit % 10
print("Остання цифра:", last_digit)

#2.6. Perimetr of the rectangle
lenth = int(input("Enter a length: "))
width = int(input("Enter a width: "))
perimeter = 2* (lenth + width)
print("Периметр:", perimeter)

#2.7. Number in column
number_line = int(input("Enter a number: "))
num4 = number_line % 10
num3 = number_line // 10 % 10
num2 = number_line // 100 % 10
num1 = number_line // 1000
print(num1)
print(num2)
print(num3)
print(num4)
