class Car:
    info = "some info"

    def __init__(self, name):
        self.name = name
        self.info = "info"

    def show_info(self):
        print(f"My car: {self.name}")

    @staticmethod
    def test_func():
        print("This is my car")


bmw = Car("BMW X5")
toyota = Car("Toyota Camry")
print(type(bmw))
print(type(toyota))

bmw.show_info()
toyota.show_info()

bmw.test_func()
toyota.test_func()

Car.test_func()

Car.show_info(bmw)
print(Car.info)
print(bmw.info)


