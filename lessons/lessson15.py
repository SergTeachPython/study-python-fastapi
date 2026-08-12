class User:
    __name: str = "no name" #private поле, доступне лише всередині цього класу
    __age: int = 0
    __secret: int = 12345

    def __init__(self, name = None, age = None):
        #застосуємо інкапсуляцію
        self.set_age(age)
        self.set_name(name)

    def set_name(self, name):
        if 2 < len(name) < 50:
            self.__name = name
        else:
            print("Incorrect name length!")

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if 18 < age < 150:
            self.__age = age
        else:
            print("Incorrect age!")

    def get_age(self):
        return self.__age

    def show_info(self):
        print(f"Name: {self.__name} age: {self.__age}")
        #print(f"Secret code: {self.__secret}")

    def __secret_info(self):
        print(f"Secret code: {self.__secret}")


vasya = User("Vasya", -44)

#print(vasya.__name)
vasya.show_info()

vasya.set_age(100)
vasya.show_info()
vasya.set_age(-100)
vasya.show_info()
#vasya.__secret_info()
vasya._User__secret_info()




