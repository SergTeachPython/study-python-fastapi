number: int = 10 + 1
print(number)
number1 = 10
print(number := 10 + number1)   #моржовий оператор

num2 = 3
result = 2 + (num1 := 4) + num2
print(result)
print(num1)

#число розкласти в стовпчик
number = 123
n1 = number // 100
n2 = number % 100 // 10
n2_v2 = number // 10 % 10
n3 = number % 10
print(n1)
print(n2)
print(n2_v2)
print(n3)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
#v1
print("Hello ", name, " You are ", age, "years old!" )
#v2 - конкатенація - складання рядків. Рядок + рядок -> один великий рядок
print("Hello " +  name + " You are " + str(age) + " years old!" )
#v3 інтерполяція рядка - вбудовування змінних у рядок завдяки функції format
print(f"Hello {name}. You are {age} years old! {(test := 12)}")
print(test)

after_ten_years = age + 10
print(after_ten_years)

number = 10
number = number + 1
print(number)

result = divmod(9, 5)
print(result)
print(type(result))

first_part, second_part = result
print(first_part)
print(second_part)


