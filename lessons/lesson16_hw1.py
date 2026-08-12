class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        s1 = self.get_square()
        s2 = other.get_square()
        return s1 == s2

    def __add__(self, other):
        s1 = self.get_square()
        s2 = other.get_square()
        return Rectangle(1, s1 + s2)

    def __mul__(self, n):
        s1 = self.get_square()
        return Rectangle(1, s1 * n)

    def __str__(self):
        return f'width = {self.width}, heigth = {self.height}, square = {self.get_square()}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print(r1)
print(r2)
print(r3)
print(r4)
