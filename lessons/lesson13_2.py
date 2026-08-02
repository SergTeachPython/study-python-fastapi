class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name} age: {self.age}")

    def __str__(self):
        return f"Name: {self.name} age: {self.age}"


user1 = Person("Vasya", 33)
user2 = Person("Petya", 44)

print(user1)
