def add_one(some_list):
    temp_str = ""
    for element in some_list:
        temp_str = temp_str + str(element)
    digit = int(temp_str)
    new_digit = digit + 1
    new_digit_str = str(new_digit)
    new_list = []
    for char in new_digit_str:
        new_list.append(int(char))
    return new_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
