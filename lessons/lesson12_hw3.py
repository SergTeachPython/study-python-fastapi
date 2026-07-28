def is_even(number):
    last_digit = int(str(number)[-1:])  #для парності числа треба, щоб остання цифра була парна
    while last_digit > 1:
        last_digit -= 2
    if last_digit == 0:
        return True
    return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')