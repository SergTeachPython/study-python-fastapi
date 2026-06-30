import random
NUMS_SIZE = random.randint(3, 10)
numbers = []
edit_numbers = []


for i in range(0,NUMS_SIZE):
    numbers.append(random.randint(1, 10))

edit_numbers.extend(numbers[:1])
edit_numbers.extend(numbers[2:3])
edit_numbers.extend(numbers[-2:-1])
print(numbers)
print(edit_numbers)




