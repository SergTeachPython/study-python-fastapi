while True:
    numb1 = int(input("Внесіть перше число: "))
    numb2 = int(input("Внесіть друге число: "))
    operation = input("Внесіть операцію над числами + - * / ")
    if operation == "+":
        print(numb1 + numb2)
    elif operation == "-":
        print(numb1 - numb2)
    elif operation == "*":
        print(numb1 * numb2)
    elif operation == "/":
        if numb2 != 0:
            print(numb1 / numb2)
        else:
            print("Ділення на нуль неможливе")

    next_operation = input("Continue calculation? (yes/no): ")
    if next_operation.lower() == "no":
        break
