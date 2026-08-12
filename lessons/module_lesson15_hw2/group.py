
from .group_limit_reached_exception import GroupLimitReachedException

class Group:

    def __init__(self, number, student_limit =3):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(f"Group limit: {self.student_limit} reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        curr_student = self.find_student(last_name)
        self.group.discard(curr_student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def __str__(self):
        all_students = f"Number: {self.number}\n"
        for curr_student in self.group:
            all_students += str(curr_student)+"\n"
        return all_students