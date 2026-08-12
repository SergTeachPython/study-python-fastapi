class User:
    __name: str = "no name"
    __age: int = 0
    __secret: int = 12345

    def __init__(self, name: str, age=None):
        self.name = name
        self.age = age

        print(self.name)

    # getter - для отримання значення приватного поля
    @property
    def name(self):
        return self.__name

    # setter -  для санкіонованого доступу до приватної змінної (поля)
    @name.setter
    def name(self, name):
        if 2 < len(name) < 50:
            self.__name = name
        else:
            print("Incorrect name length")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 < age < 150:
            self.__age = age
        else:
            print("Incorrect age length")

    #public method - публічна (доступна ззовні) функція
    def show_info(self):
        print(f"Name: {self.__name} age: {self.__age}")

    #private method - приватна (недоступна ззовні) функція
    def __secret_info(self):
        print(f"Secret code: {self.__secret}")


anton = User("Anton", -34)
anton.show_info()
anton.age = 40
test =  anton.age
anton.show_info()
anton.age = 400
anton.show_info()
print(anton.name)













