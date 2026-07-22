# def outer():
#     number = 0
#     number2 = 20
#     number3 = 30
#
#
#     print(number2)
#
#     def inner():
#         nonlocal number
#         number += 1
#         print(number)
#         print(number3)
#         number4 = 123
#         print(number4)
#         print("*" * 10)
#
#     return inner
#
# result_func1 = outer()
# result_func1()

# def additional_logic(func):
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Some logic 2")
#     return wrapper
#
# @additional_logic
# def hello():
#     print("Hello World!")
#
#
# hello()

def check_permissions(func):
    def wrapper(role):
        if role == "admin":
            print("Permission granted")
            func(role)
        else:
            print("Permission denied")
    return wrapper

@check_permissions
def get_secret_information(user_role):
    print(f"Hi, {user_role}, this is secret information.")


get_secret_information("user")
get_secret_information("admin")
