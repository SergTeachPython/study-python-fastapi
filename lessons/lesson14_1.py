class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# class Employee(Person):
#     def work(self):
#         print(f"{self.name} works!")
#
# class Company:
#     def __init__(self,employees: list[Employee]):
#         self.employee = employees
#
#
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()

# class Employee(Person):
#     def __init__(self, name, age, company):
#         super().__init__(name, age)
#         self.company = company
#
#     def show_info(self):
#         super().show_info()
#         print(f"Works in {self.company} company")
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Subject(object):
    def __init__(self, name):
        self.name = name

class MathTopicSubject(Subject):
    def __init__(self, name, test):
        super().__init__(name)
        self.test = test

class Teacher(Person):
    def __init__(self, name, age, subject: list[Subject], expirience: int):
        super().__init__(name, age)
        self.subject = subject
        self.expirience = expirience

class Student(Person):
    def __init__(self, name, age, subject: Subject):
        super().__init__(name, age)
        self.subject = subject

class Academy(object):
    def __init__(self, name, subjects: list[Subject], teachers: list[Teacher], students: list[Student]):
        self.name = name
        self.subjects: list[Subject] = subjects
        self.teachers: list[Teacher] = teachers
        self.students: list[Student] = students

current_subjects = [Subject("math"), Subject("englis"), Subject("history")]
current_teachers = [Teacher("Vasya", 33, current_subjects, 20),
                    Teacher("Petya", 33, current_subjects, 10)]

current_students = [Student("Vasya", 22, current_subjects[0]), Student("Alex", 44, current_subjects[2])]
acad = Academy("Super academy", current_subjects, current_teachers, current_students)

for teacher in acad.teachers:
    teacher.show_info()



