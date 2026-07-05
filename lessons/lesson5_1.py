import string
import random


initial_password_data =  string.ascii_letters + string.digits + string.punctuation
print(initial_password_data)

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 16

while True:
    new_password = ""

    password_length = input(f"Enter password length: from {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}: ")

    if password_length.isnumeric():
        password_length = int(password_length)
    else:
        print("Password length must be numeric")
        continue

    if MIN_PASSWORD_LENGTH <= password_length <= MAX_PASSWORD_LENGTH:
        for _ in range(password_length):
            new_password += initial_password_data[random.randint(0, len(initial_password_data)-1)]

        print(new_password)
    else:
        print(f"Password length must be between {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}")

    is_exit = input("Do you want to exit the program? (y/n): ")
    if is_exit.lower() == "y":
        print("Goodbye!")
        break






