MAX_USERNAME_LEN = 20
MIN_USERNAME_LEN = 1


def hello_user(username):
    username_length = len(username)

    if username_length > MAX_USERNAME_LEN:
        raise Exception(f"Incorrect name length provided: ({username_length})\n"
                        f"should be less than {MAX_USERNAME_LEN}\n"
                        "Please enter a valid name!")

    elif username_length <= MIN_USERNAME_LEN:
        raise Exception(f"Incorrect username length provided: ({username_length})\n"
                        f"should be more than {MIN_USERNAME_LEN}\n"
                        "Please enter a valid username!")

    print(f"Hello, {username}")


while True:
    try:
        name = input("Enter your name: ")
        hello_user(name)
        should_continue = input("Do you want to continue (y/n)?")
        if should_continue.lower() == 'n':
            break
    except Exception as e:
        print(f"Error: {e}")


