numb = int(input("Enter a integer number: "))
while numb > 9:
    length = len(str(numb)) - 1
    result = 1
    for i in range(length, 0 , -1):
        one_digit = numb // pow(10, i)
        numb %= pow(10, i)
        result *= one_digit
    numb = result * numb
print(numb)
